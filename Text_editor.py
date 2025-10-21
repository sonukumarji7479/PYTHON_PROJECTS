import tkinter as tk
import random

# --- Constants ---
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 200  # slower movement for smooth gameplay
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00ff00"  # Green
FOOD_COLOR = "#ff0000"  # Red
BACKGROUND_COLOR = "#1a1a1a"  # Dark background

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game - Sonu Kumar")
        self.window.resizable(False, False)

        self.canvas = tk.Canvas(self.window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.canvas.pack()

        self.start_game()
        self.window.mainloop()

    def start_game(self):
        self.score = 0
        self.direction = "down"
        self.snake_positions = [[100, 100], [80, 100], [60, 100]]
        self.food_position = self.set_new_food()
        self.snake_squares = []
        self.food_square = None

        self.create_objects()
        self.bind_keys()
        self.next_turn()

    def create_objects(self):
        self.canvas.delete("all")
        # Draw snake
        self.snake_squares = []
        for x, y in self.snake_positions:
            square = self.canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline="#004d00")
            self.snake_squares.append(square)
        # Draw food
        fx, fy = self.food_position
        self.food_square = self.canvas.create_rectangle(fx, fy, fx+SPACE_SIZE, fy+SPACE_SIZE, fill=FOOD_COLOR, outline="#800000")
        # Draw score
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="#ffffff", font=("Arial", 14, "bold"), tag="score")

    def set_new_food(self):
        while True:
            x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE
            if [x, y] not in self.snake_positions:
                return [x, y]

    def next_turn(self):
        x, y = self.snake_positions[0]

        # Move snake
        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        # Wrap around borders
        x = x % GAME_WIDTH
        y = y % GAME_HEIGHT

        new_head = [x, y]

        # Check collision with self
        if new_head in self.snake_positions:
            self.game_over()
            return

        self.snake_positions = [new_head] + self.snake_positions[:-1]

        # Check if food eaten
        if new_head == self.food_position:
            self.snake_positions.append(self.snake_positions[-1])
            self.score += 10
            self.food_position = self.set_new_food()

        self.create_objects()
        self.window.after(SPEED, self.next_turn)

    def change_direction(self, new_direction):
        opposites = {"up":"down", "down":"up", "left":"right", "right":"left"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def bind_keys(self):
        self.window.bind("<Up>", lambda event: self.change_direction("up"))
        self.window.bind("<Down>", lambda event: self.change_direction("down"))
        self.window.bind("<Left>", lambda event: self.change_direction("left"))
        self.window.bind("<Right>", lambda event: self.change_direction("right"))

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2-40, text="GAME OVER", fill="#ff0000", font=("Arial", 30, "bold"))
        self.canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, text=f"Score: {self.score}", fill="#ffffff", font=("Arial", 20, "bold"))
        # Play Again button
        play_again_btn = tk.Button(self.window, text="Play Again", font=("Arial", 14, "bold"), bg="#00bfff", fg="#ffffff", command=self.start_game)
        self.canvas.create_window(GAME_WIDTH/2, GAME_HEIGHT/2 + 50, window=play_again_btn)

# Start the game
SnakeGame()
