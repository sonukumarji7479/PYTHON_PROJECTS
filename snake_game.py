import tkinter as tk
from PIL import Image, ImageTk
import random

GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 200
SPACE_SIZE = 20
BACKGROUND_COLOR = "#1a1a1a"

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Realistic Snake Game - Sonu Kumar")
        self.window.resizable(False, False)
        self.canvas = tk.Canvas(self.window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.canvas.pack()

        # Temporary colored images
        from PIL import Image
        self.snake_image = Image.new("RGB", (SPACE_SIZE, SPACE_SIZE), "green")
        self.snake_photo = ImageTk.PhotoImage(self.snake_image)
        self.fruit_image = Image.new("RGB", (SPACE_SIZE, SPACE_SIZE), "red")
        self.fruit_photo = ImageTk.PhotoImage(self.fruit_image)

        self.start_game()
        self.window.mainloop()

    def start_game(self):
        self.score = 0
        self.direction = "down"
        self.snake_positions = [[100, 100], [80, 100], [60, 100]]
        self.food_position = self.set_new_food()
        self.create_objects()
        self.bind_keys()
        self.next_turn()

    def create_objects(self):
        self.canvas.delete("all")
        for x, y in self.snake_positions:
            self.canvas.create_image(x + SPACE_SIZE//2, y + SPACE_SIZE//2, image=self.snake_photo)
        fx, fy = self.food_position
        self.canvas.create_image(fx + SPACE_SIZE//2, fy + SPACE_SIZE//2, image=self.fruit_photo)
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="#ffffff", font=("Arial", 14, "bold"))

    def set_new_food(self):
        while True:
            x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE
            if [x, y] not in self.snake_positions:
                return [x, y]

    def next_turn(self):
        x, y = self.snake_positions[0]
        if self.direction == "up": y -= SPACE_SIZE
        elif self.direction == "down": y += SPACE_SIZE
        elif self.direction == "left": x -= SPACE_SIZE
        elif self.direction == "right": x += SPACE_SIZE
        x, y = x % GAME_WIDTH, y % GAME_HEIGHT
        new_head = [x, y]
        if new_head in self.snake_positions:
            self.game_over()
            return
        self.snake_positions = [new_head] + self.snake_positions[:-1]
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
        self.window.bind("<Up>", lambda e: self.change_direction("up"))
        self.window.bind("<Down>", lambda e: self.change_direction("down"))
        self.window.bind("<Left>", lambda e: self.change_direction("left"))
        self.window.bind("<Right>", lambda e: self.change_direction("right"))

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, text=f"GAME OVER! Score: {self.score}", fill="#ff0000", font=("Arial", 20, "bold"))

SnakeGame()
