from turtle import Turtle

FONT = ('Arial', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-100, 190)
        self.score1 = 0
        self.score2 = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"{self.score1}   {self.score2}", font=FONT)

    def player1_score(self):
        self.score1 += 1
        self.update_score()

    def player2_score(self):
        self.score2 += 1
        self.update_score()
