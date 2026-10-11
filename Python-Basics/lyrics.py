import os
import re
import sys
import time

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

import pygame

TIMESTAMP_RE = re.compile(r"\[(?P<min>\d+):(?P<sec>\d{2})(?:[.:](?P<cs>\d{1,3}))?\]")
ANSI_BOLD = "\033[1m"
ANSI_REVERSE = "\033[7m"
ANSI_RESET = "\033[0m"
ANSI_CLEAR_LINE = "\033[2K"
ANSI_MOVE_UP = lambda n: f"\033[{n}A"
ANSI_MOVE_DOWN = lambda n: f"\033[{n}B"


def parse_lyrics(path, song_duration=None):
    lyrics = []
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    for raw in lines:
        matches = list(TIMESTAMP_RE.finditer(raw))
        if not matches:
            lyrics.append((None, raw))
            continue

        text = TIMESTAMP_RE.sub('', raw).strip()
        for match in matches:
            minute = int(match.group('min'))
            second = int(match.group('sec'))
            centis = match.group('cs') or '0'
            if len(centis) == 1:
                fraction = int(centis) / 10.0
            elif len(centis) == 2:
                fraction = int(centis) / 100.0
            else:
                fraction = int(centis) / 1000.0
            timestamp = minute * 60 + second + fraction
            lyrics.append((timestamp, text))

    lyrics.sort(key=lambda item: item[0] if item[0] is not None else float('inf'))
    if not any(ts is not None for ts, _ in lyrics):
        if song_duration is None or not lyrics:
            return None
        interval = song_duration / len(lyrics)
        return [(i * interval, text) for i, (_, text) in enumerate(lyrics)]

    parsed = []
    last_time = 0.0
    for timestamp, text in lyrics:
        if timestamp is None:
            timestamp = last_time + 3.0
        parsed.append((timestamp, text))
        last_time = timestamp

    return parsed


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor_up(lines):
    if lines > 0:
        sys.stdout.write(ANSI_MOVE_UP(lines))


def move_cursor_down(lines):
    if lines > 0:
        sys.stdout.write(ANSI_MOVE_DOWN(lines))


def highlight_word(text, word_index):
    words = text.split(' ')
    highlighted = []
    for idx, word in enumerate(words):
        if idx == word_index:
            highlighted.append(f"{ANSI_BOLD}{ANSI_REVERSE}{word}{ANSI_RESET}")
        else:
            highlighted.append(word)
    return ' '.join(highlighted)


def format_time(seconds):
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def choose_file(prompt_text, default_name):
    if os.path.exists(default_name):
        answer = input(f"{prompt_text} [{default_name}] (Enter to accept): ").strip()
        if not answer:
            return default_name
        return answer

    path = input(f"{prompt_text}: ").strip()
    return path


_last_window_height = 0


def print_lyrics_window(lyrics, current_index, current_word=0):
    global _last_window_height

    start = max(0, current_index - 3)
    end = min(len(lyrics), current_index + 5)
    window_lines = ["=== Lyrics Scroller ===", "Press Ctrl+C to stop."]
    for idx in range(start, end):
        prefix = ">>" if idx == current_index else "  "
        text = lyrics[idx][1]
        if idx == current_index:
            text = highlight_word(text, current_word)
        window_lines.append(f"{prefix} {text}")
    window_lines.append("")

    if _last_window_height:
        move_cursor_up(_last_window_height)
    for line in window_lines:
        sys.stdout.write(ANSI_CLEAR_LINE + "\r" + line + "\n")
    sys.stdout.flush()
    _last_window_height = len(window_lines)


def main():
    song_file = None
    lyrics_file = None
    offset_seconds = 0.0

    if len(sys.argv) >= 2:
        song_file = sys.argv[1]
    if len(sys.argv) >= 3:
        lyrics_file = sys.argv[2]
    if len(sys.argv) >= 4:
        try:
            offset_seconds = float(sys.argv[3])
        except ValueError:
            print(f"Invalid offset value: {sys.argv[3]}. Using 0.0s.")
            offset_seconds = 0.0

    if not song_file:
        song_file = choose_file("Song file path", "song.mp3")
    if not lyrics_file:
        default_lyrics = "lyrics.lrc" if os.path.exists("lyrics.lrc") else "lyrics.txt"
        lyrics_file = choose_file("Lyrics file path", default_lyrics)

    if not os.path.exists(song_file):
        print(f"Audio file not found: {song_file}")
        return
    if not os.path.exists(lyrics_file):
        print(f"Lyrics file not found: {lyrics_file}")
        return

    try:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(song_file)
        song_duration = sound.get_length()
        pygame.mixer.music.load(song_file)
    except pygame.error as error:
        print(f"Unable to load audio file: {error}")
        return

    lyrics = parse_lyrics(lyrics_file, song_duration=song_duration)
    if lyrics is None:
        print("Lyrics file has no timestamps. For exact sync, please use a timestamped .lrc or .txt file.")
        print("Example: [00:12.34]Hello world")
        return

    if not any(TIMESTAMP_RE.search(line) for line in open(lyrics_file, 'r', encoding='utf-8')):
        print("No timestamps found in lyrics. Lyrics will be evenly distributed across the song duration.")

    line_durations = []
    for idx in range(len(lyrics)):
        start = lyrics[idx][0]
        if idx + 1 < len(lyrics):
            end = lyrics[idx + 1][0]
        else:
            end = song_duration if song_duration > start else start + 3.0
        line_durations.append(max(end - start, 0.5))

    try:
        pygame.mixer.music.play()
    except pygame.error as error:
        print(f"Unable to play audio: {error}")
        return

    current_index = -1
    current_word = -1
    start_time = time.monotonic()

    try:
        while pygame.mixer.music.get_busy():
            pos_ms = pygame.mixer.music.get_pos()
            if pos_ms >= 0:
                current_seconds = pos_ms / 1000.0
            else:
                current_seconds = time.monotonic() - start_time

            current_seconds += offset_seconds

            next_index = current_index
            while next_index + 1 < len(lyrics) and current_seconds >= lyrics[next_index + 1][0]:
                next_index += 1

            if next_index < 0:
                next_index = 0

            line_text = lyrics[next_index][1]
            elapsed = max(0.0, current_seconds - lyrics[next_index][0])
            duration = line_durations[next_index]
            words = line_text.split(' ')
            if words:
                word_index = min(len(words) - 1, int((elapsed / duration) * len(words)))
            else:
                word_index = 0

            if next_index != current_index or word_index != current_word:
                current_index = next_index
                current_word = word_index
                print_lyrics_window(lyrics, current_index, current_word)

            time.sleep(0.03)

        print("\nPlayback finished.")
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nStopped by user.")


if __name__ == '__main__':
    main()
