from turtle import Turtle, Screen

#draw simple square

tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()