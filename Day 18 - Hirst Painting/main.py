# In todays project I used my GUI skills
# I learned today to make a Hirst painting.
# I also learned more on importing packages that
# aren't originally in python

import colorgram
import random
from turtle import Turtle, Screen, colormode

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

list_of_colors = []
for color in range(len(rgb_colors)):
    red = rgb_colors[color].r
    green = rgb_colors[color].g
    blue = rgb_colors[color].b

    temp_tuple = (red, green, blue)
    list_of_colors.append(temp_tuple)

colormode(255)
tim = Turtle()
new_y = -300
tim.up()
for _ in range(10):
    tim.setx(-300)
    tim.sety(new_y)
    for _ in range(10):
        tim.color(random.choice(list_of_colors))
        tim.dot(30)
        tim.forward(50)
    new_y += 50

screen = Screen()
screen.exitonclick()
