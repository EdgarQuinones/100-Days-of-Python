from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("white")
        self.y_speed = 15
        self.x_speed = 15
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_speed
        new_x = self.xcor() + self.x_speed
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_speed *= -1

    def bounce_horizontal(self):
        self.x_speed *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.bounce_horizontal()
        self.move_speed = 0.1

    # def increase_speed(self):
    #     if self.x_speed < 0:
    #         self.x_speed *= -1
    #         self.x_speed += 1
    #         self.x_speed *= -1
    #     else:
    #         self.x_speed += 1
