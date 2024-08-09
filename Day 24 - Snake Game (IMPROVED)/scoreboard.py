from turtle import Turtle

FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-100, 270)
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(-50, 0)
    #     self.write("Game Over", font=FONT)
