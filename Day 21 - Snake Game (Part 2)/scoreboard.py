from turtle import Turtle

FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-50, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=FONT)
