from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.make_body()
        self.head = self.snake_body[0]

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.speed("slowest")
        new_snake.goto(position)
        self.snake_body.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[segment].goto(self.snake_body[segment - 1].xcor(), self.snake_body[segment - 1].ycor())
        self.head.forward(20)

    def make_body(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.make_body()
        self.head = self.snake_body[0]
