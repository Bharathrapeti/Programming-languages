from tkinter import *

# Function to handle the Tic-Tac-Toe logic
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def button_click(row, col):
    if board[row][col] == "" and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        winner = check_winner()
        if winner:
            status_label.config(text=f"Player {winner} Wins!")
            global game_over
            game_over = True
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            status_label.config(text="It's a Draw!")
            game_over = True
        else:
            switch_player()

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Player {current_player}'s Turn")

def restart_game():
    global board, game_over, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    game_over = False
    current_player = "X"
    status_label.config(text="Player X's Turn")
    
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

# Set up the main window
root = Tk()
root.title("Tic-Tac-Toe Game")

# Game state variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

# Create the Tic-Tac-Toe buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(root, text="", font=("Arial", 40), width=5, height=2,
                                   command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Create the status label
status_label = Label(root, text="Player X's Turn", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

# Create the Restart button
restart_button = Button(root, text="Restart", font=("Arial", 14), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
