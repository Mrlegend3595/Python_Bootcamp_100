from turtle import Turtle

PADDLE1_POSITIONS = [(380,0),(380,-20),(380,-40),(380,-60),(380,-80)]
PADDLE2_POSITIONS = [(-380,0),(-380,-20),(-380,-40),(-380,-60),(-380,-80)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270

class Paddle:
    def __init__(self, number_paddle):
        self.number_paddle = number_paddle
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]


    def create_paddle(self):
        for position in range(len(PADDLE1_POSITIONS)):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            if self.number_paddle == 1:
                segment.goto(PADDLE1_POSITIONS[position])
            else:
                segment.goto(PADDLE2_POSITIONS[position])
            segment.setheading(DOWN)
            self.segments.append(segment)

    def move(self):

        if self.head.ycor() > 300 and self.head.heading() != DOWN:
            self.head.forward(0)
        elif self.head.ycor() < -300 and self.head.heading() != UP:
            self.head.forward(0)
        else:
            for segment in range(len(self.segments) -1 , 0 ,-1):
                new_x = self.segments[segment - 1].xcor()
                new_y = self.segments[segment - 1].ycor()
                self.segments[segment].goto(new_x, new_y)

            self.head.forward(MOVE_DISTANCE)


    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)
