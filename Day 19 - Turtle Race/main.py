# Todays project uses the skill of
# OOP and mutiple objects to make a working
# turtle race. It combines OOP and the turtle
# GUI to make 6 individual turtles on a race
# track going at different speeds.

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [175, 122, 46, -20, -86, -152]
all_turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

winner = ""
race_is_over = False
while not race_is_over:
    for new_turtle in all_turtles:
        new_turtle.forward(random.randint(a=0, b=10))
        if new_turtle.xcor() >= 230:
            race_is_over = True
            winner = new_turtle
print(f"The winner is {winner.pencolor()}")
if guess == winner.pencolor():
    print("You win!")
else:
    print("You Lost!")
screen.exitonclick()
