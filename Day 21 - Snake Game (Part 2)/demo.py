class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Gills")

    def swim(self):
        print("Swish, swish")


nemo = Fish()
nemo.breathe()

from turtle import Turtle, Screen

text = Turtle()
text.hideturtle()
text.penup()
text.color("red")
text.write("Hello wrld", True, align='center')
screen = Screen()
screen.exitonclick()
