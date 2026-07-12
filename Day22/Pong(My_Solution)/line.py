from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.create_line()

    def create_line(self):
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        self.pendown()

        y = -300
        while y < 300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
            y += 20


