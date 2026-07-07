import turtle
from turtle import Screen, Turtle

#My solution
# from random import choice
# colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
#
#
# tim = Turtle()
# tim.width(3)
#
# def left():
#     tim.color(choice(colors))
#     tim.left(90)
#     tim.forward(20)
#
# def right():
#     tim.color(choice(colors))
#     tim.right(90)
#     tim.forward(20)
#
# def up():
#     tim.color(choice(colors))
#     tim.forward(20)
#
# def down():
#     tim.color(choice(colors))
#     tim.right(180)
#     tim.forward(20)
#
#
# actions = {"left": left,
#            "right": right,
#            "up": up,
#            "down": down}
#
# for _ in range(100):
#     action = choice(list(actions.keys()))
#     actions[action]()
#______________________________________________
import random
timmy = Turtle()
screen = Screen()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'cyan']
directions = [0, 90, 180, 270]
timmy.pensize(10)
screen.bgcolor("black")


timmy.speed(10)

for _ in range(100):
    # timmy.color(random.choice(colors))
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen.exitonclick()
