from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 30
STARTING_X_POSITION = 320
RANDOM_Y_POSITION_TOP = 250
RANDOM_Y_POSITION_BOTTOM = -250
ENDING_X_POSITION = -320
RANDOM_LEFT_X = -280
RANDOM_RIGHT_X = 280


class CarManager:
    def __init__(self):
        self.cars = []
        self.setup_cars()
        self.speed = STARTING_MOVE_DISTANCE

    def setup_cars(self):
        for _ in range(NUMBER_OF_CARS):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=.8, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            random_position = (random.randint(RANDOM_LEFT_X, RANDOM_RIGHT_X),
                               random.randint(RANDOM_Y_POSITION_BOTTOM, RANDOM_Y_POSITION_TOP))
            new_car.goto(random_position)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < ENDING_X_POSITION:
                car.color(random.choice(COLORS))
                random_position = (300,
                                   random.randint(RANDOM_Y_POSITION_BOTTOM, RANDOM_Y_POSITION_TOP))
                car.goto(random_position)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
