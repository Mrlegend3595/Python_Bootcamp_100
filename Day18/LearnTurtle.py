# Learn Reading Document
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()


#Types of import
#1: import {Package}
#2: from {Package} import {Class or variable or ...}
#3: from {Package} import *
#4: import {Package} as {new name package}
import heroes
print(heroes.gen())
