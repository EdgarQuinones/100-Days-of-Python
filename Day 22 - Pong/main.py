from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the screen of the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Setting up the border in the middle
border = Turtle()
border.color("white")
border.penup()
border.goto(0, 300)
border.setheading(270)
for _ in range(20):
    border.pendown()
    border.forward(20)
    border.penup()
    border.forward(20)

# Creates objects
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# User controls for both paddles
screen.onkeypress(key='w', fun=paddle_2.up)
screen.onkeypress(key='s', fun=paddle_2.down)
screen.onkeypress(key='Up', fun=paddle_1.up)
screen.onkeypress(key='Down', fun=paddle_1.down)

game_over = False
while not game_over:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect ball collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    # Detect if ball collides with paddle, or misses and player scores
    if ball.distance(paddle_1) < 50 and ball.xcor() >= 330:
        ball.bounce_horizontal()
        # ball.increase_speed()
    elif ball.xcor() >= 390:
        scoreboard.player2_score()
        ball.reset()
    if ball.distance(paddle_2) < 50 and ball.xcor() <= -330:
        ball.bounce_horizontal()
        # ball.increase_speed()
    elif ball.xcor() <= -390:
        scoreboard.player1_score()
        ball.reset()

screen.exitonclick()
