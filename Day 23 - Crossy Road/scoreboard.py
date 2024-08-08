from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-280, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def new_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write("Game Over", font=FONT)
