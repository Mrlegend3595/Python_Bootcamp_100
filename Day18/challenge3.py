from turtle import Screen, Turtle
from random import choice
tim = Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    tim.color(choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
