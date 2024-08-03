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

# Got rid of the background colors
list_of_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
                  (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
                  (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
                  (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
                  (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


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
