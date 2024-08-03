from turtle import Turtle, Screen, colormode
import random

# Options of importing
# from turtle import *
# import turtle as t
# bob = t.Turtle()

tim = Turtle()
tim.shape("turtle")
tim.color("DarkRed")

# Challenge 1 - Draw a Square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

# Challenge 2 - Draw a Dashed Line
for _ in range(10):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()

# Challenge 3 - Draw 7 shapes each with different colors
color_list = ["medium spring green", "coral", "antique white", "medium slate blue", "medium violet red",
              "pale violet red"]
for side in range(3, 11):
    degrees = 360 / side
    tim.pencolor(random.choice(color_list))
    for _ in range(side):
        tim.forward(100)
        tim.right(degrees)


# Challenge 4 - Random walk
def change_color():
    temp_colors = [0, 0, 0]
    for color in range(len(temp_colors)):
        temp_colors[color] = random.randint(0, 255)
    return tuple(temp_colors)


colormode(255)
tim.pensize(15)
tim.speed("fastest")
tim.shape("classic")
directions = [0, 90, 180, 270]
for _ in range(100):
    tim.pencolor(change_color())
    tim.setheading(random.choice(directions))
    tim.forward(40)

screen = Screen()
screen.exitonclick()


# Challenge 5 - Spirograph
def change_color():
    temp_colors = [0, 0, 0]
    for color in range(len(temp_colors)):
        temp_colors[color] = random.randint(0, 255)
    return tuple(temp_colors)


colormode(255)
for _ in range(72):
    tim.color(change_color())
    tim.speed("fastest")
    tim.circle(100)
    tim.right(5)

screen = Screen()
screen.exitonclick()
