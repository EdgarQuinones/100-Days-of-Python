import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Sets up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Sets up objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


# Set up starting and finishing line
def make_line(x, y):
    border.goto(x, y)
    for _ in range(15):
        border.pendown()
        border.forward(20)
        border.penup()
        border.forward(20)


border = Turtle()
border.hideturtle()
border.penup()
border.color("black")
make_line(-300, 270)
make_line(-300, -260)


# Sets up user input
screen.listen()
screen.onkeypress(key='w', fun=player.move)

# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 270:
        scoreboard.new_level()
        car_manager.speed_up()
        player.reset_position()

screen.exitonclick()
