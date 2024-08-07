from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)

    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
