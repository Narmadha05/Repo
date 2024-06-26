import tkinter
import winsound  # Import winsound module for playing sound effects on Windows

# Initialize scores
score_x = 0
score_o = 0

# Define sound file paths
placed_tile_sound = "tile_placed.wav"
win_sound = "win.wav"
tie_sound = "tie.wav"

def set_tile(row, column):
    global curr_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player
    winsound.PlaySound(placed_tile_sound, winsound.SND_FILENAME)  # Play sound when tile is placed

    # Check for winner after each move
    check_winner()

    # Switch player
    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = f"{curr_player}'s turn - Scores: X {score_x} - O {score_o}"


def check_winner():
    global turns, game_over, score_x, score_o

    turns += 1

    # Check rows for a winner
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            winner = board[row][0]["text"]
            label.config(text=f"{winner} is the winner!", foreground=color_yellow)
            update_scores(winner)
            winsound.PlaySound(win_sound, winsound.SND_FILENAME)  # Play win sound effect
            game_over = True
            return

    # Check columns for a winner
    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
                and board[0][col]["text"] != ""):
            winner = board[0][col]["text"]
            label.config(text=f"{winner} is the winner!", foreground=color_yellow)
            update_scores(winner)
            winsound.PlaySound(win_sound, winsound.SND_FILENAME)  # Play win sound effect
            game_over = True
            return

    # Check diagonals for a winner
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        winner = board[0][0]["text"]
        label.config(text=f"{winner} is the winner!", foreground=color_yellow)
        update_scores(winner)
        winsound.PlaySound(win_sound, winsound.SND_FILENAME)  # Play win sound effect
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        winner = board[0][2]["text"]
        label.config(text=f"{winner} is the winner!", foreground=color_yellow)
        update_scores(winner)
        winsound.PlaySound(win_sound, winsound.SND_FILENAME)  # Play win sound effect
        game_over = True
        return

    # Check for tie
    if turns == 9:
        label.config(text="Tie!", foreground=color_yellow)
        winsound.PlaySound(tie_sound, winsound.SND_FILENAME)  # Play tie sound effect
        game_over = True


def update_scores(winner):
    global score_x, score_o
    if winner == 'X':
        score_x += 1
    else:
        score_o += 1


def new_game():
    global turns, game_over, curr_player

    turns = 0
    game_over = False
    curr_player = playerX

    label.config(text=f"{curr_player}'s turn - Scores: X {score_x} - O {score_o}", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_pink)


# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#8B008B"
color_yellow = "#FF1493"
color_light_pink = "#EE82EE"
color_pink = "#FFB6C1"

turns = 0
game_over = False 

# Window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=f"{curr_player}'s turn - Scores: X {score_x} - O {score_o}", font=("Consolas", 20), background=color_pink, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_pink, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_pink,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()