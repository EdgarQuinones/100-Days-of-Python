# Challenge - Etch A Sketch
from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(15)


def turn_right():
    tim.right(15)


def clear_drawing():
    tim.home()
    tim.clear()
    tim.setheading(0)


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(key="Up", fun=move_forward)
screen.onkeypress(key="Down", fun=move_backward)
screen.onkeypress(key="Left", fun=turn_left)
screen.onkeypress(key="Right", fun=turn_right)
screen.onkeyrelease(key="space", fun=clear_drawing)
screen.exitonclick()
