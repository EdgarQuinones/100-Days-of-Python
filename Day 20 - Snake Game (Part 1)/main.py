# Snake game

from turtle import Turtle, Screen


def heading_allowed(current_heading, new_heading):
    if (current_heading + 180) != new_heading and (current_heading - 180) != new_heading:
        return True
    else:
        return False


def move_up():
    if heading_allowed(current_heading=snake_head.heading(), new_heading=90):
        snake_head.speed("fastest")
        snake_head.setheading(90)
        snake_head.speed("slowest")


def move_down():
    if heading_allowed(current_heading=snake_head.heading(), new_heading=270):
        snake_head.speed("fastest")
        snake_head.setheading(270)
        snake_head.speed("slowest")


def move_left():
    if heading_allowed(current_heading=snake_head.heading(), new_heading=180):
        snake_head.speed("fastest")
        snake_head.setheading(180)
        snake_head.speed("slowest")


def move_right():
    if heading_allowed(current_heading=snake_head.heading(), new_heading=0):
        snake_head.speed("fastest")
        snake_head.setheading(0)
        snake_head.speed("slowest")


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)

full_snake_body = []
body_location = 0
snake_shape = "square"

# Starting Snake Body
snake_head = Turtle(snake_shape)
snake_head.penup()
snake_head.speed("slowest")

body_location -= 20
snake_body = Turtle(snake_shape)
snake_body.penup()
snake_body.setposition(x=body_location, y=0)

full_snake_body.append(snake_head)
full_snake_body.append(snake_body)

for _ in range(500):
    for index in range(len(full_snake_body)):
        full_snake_body[index].forward(10)
        if index != 0:
            snake_head_heading = snake_head.heading()
            snake_head_x = snake_head.xcor()
            snake_head_y = snake_head.ycor()
            if snake_head_heading == 180:
                full_snake_body[index].setx(snake_head_x + 20)
            elif snake_head_heading == 0:
                full_snake_body[index].setx(snake_head_x - 20)
            elif snake_head_heading == 90:
                full_snake_body[index].sety(snake_head_y - 20)
            else:
                full_snake_body[index].sety(snake_head_y + 20)

screen.exitonclick()
