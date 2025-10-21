import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe: Red vs Green")
root.geometry("400x450")

current_player = "Red"
board = [""] * 9
buttons = []

# Create a canvas for drawing winning line
canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=3)

# Draw buttons on top of canvas
def create_buttons():
    for i in range(9):
        row = i // 3
        col = i % 3
        btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda i=i: on_click(i))
        btn.place(x=col*133, y=row*133)  # position over canvas
        buttons.append(btn)

def draw_winning_line(combo):
    a, b, c = combo
    coords = {
        0: (66, 66), 1: (200, 66), 2: (333, 66),
        3: (66, 200), 4: (200, 200), 5: (333, 200),
        6: (66, 333), 7: (200, 333), 8: (333, 333)
    }
    x1, y1 = coords[a]
    x2, y2 = coords[c]
    canvas.create_line(x1, y1, x2, y2, width=5, fill="blue")

def check_winner():
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            winner = "Red Team" if board[a] == "X" else "Green Team"
            draw_winning_line(combo)
            messagebox.showinfo("Winner!", f"{winner} wins the match!")
            reset_board()
            return True
    if "" not in board:
        messagebox.showinfo("Draw", "Match Tie!")
        reset_board()
        return True
    return False

def on_click(index):
    global current_player
    if board[index] == "":
        if current_player == "Red":
            buttons[index].config(text="X", fg="red")
            board[index] = "X"
            current_player = "Green"
        else:
            buttons[index].config(text="O", fg="green")
            board[index] = "O"
            current_player = "Red"
        check_winner()

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "Red"
    canvas.delete("all")
    for button in buttons:
        button.config(text="")

create_buttons()
root.mainloop()
