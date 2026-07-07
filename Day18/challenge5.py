# from turtle import Turtle, Screen
# import random as rd
#
# def random_color():
#     r = rd.randint(0,255)
#     g = rd.randint(0,255)
#     b = rd.randint(0,255)
#     return r,g,b
#
#
# turtle.colormode(255)
# timmy = Turtle()
# screen = Screen()
#
# timmy.speed("fastest")
# angle = 5
#
#
# for i in range(int(365/angle)):
#     timmy.color(random_color())
#     timmy.circle(80)
#     timmy.left(angle)
#


#________________________________________
import turtle
from turtle import Turtle, Screen
import random as rd

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    return r,g,b

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)



turtle.colormode(255)
timmy = Turtle()
screen = Screen()
timmy.speed("fastest")

draw_spirograph(5)
screen.exitonclick()