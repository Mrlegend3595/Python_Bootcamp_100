from turtle import Turtle
import random

BALL_SPEED = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_ball()


    def reset_ball(self):
        self.clear()
        self.goto(0, 0)
        self.setheading(random.randint(45,322))

    def move(self):
        self.forward(BALL_SPEED)