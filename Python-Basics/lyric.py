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


# ============================================================
# FILE CONFIGURATION
# ============================================================

# Automatically find the folder where lyric.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Your song and lyrics files
SONG_FILE = os.path.join(BASE_DIR, "they_call.mp3")
LYRICS_FILE = os.path.join(BASE_DIR, "lyrics.lrc")


# ============================================================
# LRC TIMESTAMP REGEX
# Supports:
# [00:12]
# [00:12.34]
# [00:12:34]
# ============================================================

TIMESTAMP_RE = re.compile(
    r"\[(?P<min>\d+):(?P<sec>\d{2})(?:[.:](?P<cs>\d{1,3}))?\]"
)


# ============================================================
# ANSI TERMINAL SETTINGS
# ============================================================

ANSI_BOLD = "\033[1m"
ANSI_REVERSE = "\033[7m"
ANSI_RESET = "\033[0m"
ANSI_CLEAR_LINE = "\033[2K"

ANSI_MOVE_UP = lambda n: f"\033[{n}A"
ANSI_MOVE_DOWN = lambda n: f"\033[{n}B"


# ============================================================
# PARSE LYRICS
# ============================================================

def parse_lyrics(path, song_duration=None):

    lyrics = []

    with open(path, "r", encoding="utf-8") as f:
        lines = [
            line.strip()
            for line in f
            if line.strip()
        ]

    for raw in lines:

        matches = list(
            TIMESTAMP_RE.finditer(raw)
        )

        # No timestamp
        if not matches:
            lyrics.append((None, raw))
            continue

        # Remove timestamps from lyric text
        text = TIMESTAMP_RE.sub(
            "",
            raw
        ).strip()

        for match in matches:

            minute = int(
                match.group("min")
            )

            second = int(
                match.group("sec")
            )

            cs = match.group("cs") or "0"

            if len(cs) == 1:
                fraction = int(cs) / 10.0

            elif len(cs) == 2:
                fraction = int(cs) / 100.0

            else:
                fraction = int(cs) / 1000.0

            timestamp = (
                minute * 60
                + second
                + fraction
            )

            lyrics.append(
                (timestamp, text)
            )

    # Sort lyrics by timestamp
    lyrics.sort(
        key=lambda item:
        item[0]
        if item[0] is not None
        else float("inf")
    )

    # ========================================================
    # NO TIMESTAMPS
    # ========================================================

    if not any(
        ts is not None
        for ts, _ in lyrics
    ):

        if song_duration is None or not lyrics:
            return None

        # Spread lyrics evenly
        interval = (
            song_duration
            / len(lyrics)
        )

        return [
            (
                i * interval,
                text
            )
            for i, (_, text)
            in enumerate(lyrics)
        ]

    # ========================================================
    # HANDLE MISSING TIMESTAMPS
    # ========================================================

    parsed = []

    last_time = 0.0

    for timestamp, text in lyrics:

        if timestamp is None:
            timestamp = last_time + 3.0

        parsed.append(
            (timestamp, text)
        )

        last_time = timestamp

    return parsed


# ============================================================
# CLEAR TERMINAL
# ============================================================

def clear_terminal():

    os.system(
        "cls"
        if os.name == "nt"
        else "clear"
    )


# ============================================================
# MOVE CURSOR UP
# ============================================================

def move_cursor_up(lines):

    if lines > 0:
        sys.stdout.write(
            ANSI_MOVE_UP(lines)
        )


# ============================================================
# MOVE CURSOR DOWN
# ============================================================

def move_cursor_down(lines):

    if lines > 0:
        sys.stdout.write(
            ANSI_MOVE_DOWN(lines)
        )


# ============================================================
# HIGHLIGHT CURRENT WORD
# ============================================================

def highlight_word(
    text,
    word_index
):

    words = text.split(" ")

    highlighted = []

    for index, word in enumerate(words):

        if index == word_index:

            highlighted.append(
                f"{ANSI_BOLD}"
                f"{ANSI_REVERSE}"
                f"{word}"
                f"{ANSI_RESET}"
            )

        else:

            highlighted.append(word)

    return " ".join(highlighted)


# ============================================================
# FORMAT TIME
# ============================================================

def format_time(seconds):

    minutes = int(
        seconds // 60
    )

    secs = int(
        seconds % 60
    )

    return f"{minutes:02d}:{secs:02d}"


# ============================================================
# LYRICS WINDOW
# ============================================================

_last_window_height = 0


def print_lyrics_window(
    lyrics,
    current_index,
    current_word=0
):

    global _last_window_height

    # Show 3 previous lines
    # and 4 upcoming lines
    start = max(
        0,
        current_index - 3
    )

    end = min(
        len(lyrics),
        current_index + 5
    )

    window_lines = [
        "========================================",
        "             🎵 LYRICS PLAYER",
        "========================================",
        "Press Ctrl+C to stop.",
        ""
    ]

    for index in range(
        start,
        end
    ):

        if index == current_index:
            prefix = ">>"
        else:
            prefix = "  "

        text = lyrics[index][1]

        # Highlight current word
        if index == current_index:

            text = highlight_word(
                text,
                current_word
            )

        window_lines.append(
            f"{prefix} {text}"
        )

    window_lines.append("")

    # Move cursor to previous window
    if _last_window_height:

        move_cursor_up(
            _last_window_height
        )

    # Print updated window
    for line in window_lines:

        sys.stdout.write(
            ANSI_CLEAR_LINE
            + "\r"
            + line
            + "\n"
        )

    sys.stdout.flush()

    _last_window_height = len(
        window_lines
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # --------------------------------------------------------
    # YOUR FILES
    # --------------------------------------------------------

    song_file = SONG_FILE
    lyrics_file = LYRICS_FILE

    # You can change this if lyrics appear
    # slightly early or late.
    offset_seconds = 0.0


    # ========================================================
    # CHECK SONG
    # ========================================================

    if not os.path.isfile(song_file):

        print(
            "\n❌ Song file not found!"
        )

        print(
            f"\nExpected:"
        )

        print(
            f"  {song_file}"
        )

        print(
            "\nMake sure 'they_call.mp3' "
            "is in the same folder as lyric.py."
        )

        return


    # ========================================================
    # CHECK LYRICS
    # ========================================================

    if not os.path.isfile(lyrics_file):

        print(
            "\n❌ Lyrics file not found!"
        )

        print(
            f"\nExpected:"
        )

        print(
            f"  {lyrics_file}"
        )

        print(
            "\nMake sure 'lyrics.lrc' "
            "is in the same folder as lyric.py."
        )

        return


    # ========================================================
    # DISPLAY FILE INFORMATION
    # ========================================================

    print()
    print(
        "========================================"
    )
    print(
        "             🎵 LYRICS PLAYER"
    )
    print(
        "========================================"
    )

    print(
        f"\n🎵 Song   : "
        f"{os.path.basename(song_file)}"
    )

    print(
        f"📝 Lyrics : "
        f"{os.path.basename(lyrics_file)}"
    )

    print(
        "========================================"
    )


    # ========================================================
    # INITIALIZE PYGAME
    # ========================================================

    try:

        pygame.mixer.init()

        sound = pygame.mixer.Sound(
            song_file
        )

        song_duration = sound.get_length()

        pygame.mixer.music.load(
            song_file
        )

    except pygame.error as error:

        print(
            "\n❌ Unable to load song."
        )

        print(
            f"Error: {error}"
        )

        return


    # ========================================================
    # LOAD LYRICS
    # ========================================================

    try:

        lyrics = parse_lyrics(
            lyrics_file,
            song_duration
        )

    except Exception as error:

        print(
            "\n❌ Unable to read lyrics."
        )

        print(
            f"Error: {error}"
        )

        pygame.mixer.quit()

        return


    if lyrics is None:

        print(
            "\n❌ No usable lyrics found."
        )

        pygame.mixer.quit()

        return


    # ========================================================
    # CHECK TIMESTAMPS
    # ========================================================

    with open(
        lyrics_file,
        "r",
        encoding="utf-8"
    ) as f:

        has_timestamps = any(
            TIMESTAMP_RE.search(line)
            for line in f
        )


    if not has_timestamps:

        print(
            "\n⚠️ No timestamps found."
        )

        print(
            "Lyrics will be distributed "
            "across the song automatically."
        )


    # ========================================================
    # CALCULATE LINE DURATIONS
    # ========================================================

    line_durations = []

    for index in range(
        len(lyrics)
    ):

        start = lyrics[index][0]

        if index + 1 < len(lyrics):

            end = lyrics[
                index + 1
            ][0]

        else:

            end = (
                song_duration
                if song_duration > start
                else start + 3.0
            )

        duration = max(
            end - start,
            0.5
        )

        line_durations.append(
            duration
        )


    # ========================================================
    # START MUSIC
    # ========================================================

    try:

        pygame.mixer.music.play()

    except pygame.error as error:

        print(
            "\n❌ Unable to play song."
        )

        print(
            f"Error: {error}"
        )

        pygame.mixer.quit()

        return


    print(
        "\n▶️ Playing...\n"
    )


    # ========================================================
    # VARIABLES
    # ========================================================

    current_index = -1
    current_word = -1

    start_time = time.monotonic()


    # ========================================================
    # SYNCHRONIZE LYRICS
    # ========================================================

    try:

        while pygame.mixer.music.get_busy():

            # Get current song position
            pos_ms = (
                pygame.mixer.music.get_pos()
            )

            if pos_ms >= 0:

                current_seconds = (
                    pos_ms / 1000.0
                )

            else:

                current_seconds = (
                    time.monotonic()
                    - start_time
                )


            # Apply synchronization offset
            current_seconds += (
                offset_seconds
            )


            # ------------------------------------------------
            # FIND CURRENT LYRIC
            # ------------------------------------------------

            next_index = current_index

            while (
                next_index + 1
                < len(lyrics)
                and current_seconds
                >= lyrics[
                    next_index + 1
                ][0]
            ):

                next_index += 1


            if next_index < 0:

                next_index = 0


            # ------------------------------------------------
            # CURRENT LINE
            # ------------------------------------------------

            line_text = lyrics[
                next_index
            ][1]

            elapsed = max(
                0.0,
                current_seconds
                - lyrics[
                    next_index
                ][0]
            )

            duration = line_durations[
                next_index
            ]


            # ------------------------------------------------
            # CURRENT WORD
            # ------------------------------------------------

            words = line_text.split(" ")

            if words:

                word_index = min(
                    len(words) - 1,
                    int(
                        (
                            elapsed
                            / duration
                        )
                        * len(words)
                    )
                )

            else:

                word_index = 0


            # ------------------------------------------------
            # UPDATE SCREEN
            # ------------------------------------------------

            if (
                next_index
                != current_index
                or word_index
                != current_word
            ):

                current_index = (
                    next_index
                )

                current_word = (
                    word_index
                )

                print_lyrics_window(
                    lyrics,
                    current_index,
                    current_word
                )


            # Update every 30 milliseconds
            time.sleep(0.03)


        # ====================================================
        # FINISHED
        # ====================================================

        print(
            "\n\n🎵 Playback finished."
        )


    except KeyboardInterrupt:

        pygame.mixer.music.stop()

        print(
            "\n\n⏹️ Stopped by user."
        )


    finally:

        pygame.mixer.quit()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()
