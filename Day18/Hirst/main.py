import turtle as t
import random as rn
from use_colorgram import color_list


timmy = t.Turtle()
t.colormode(255)

#ُMy Solution
# timmy.speed("fastest")
# timmy.pensize(20)
# def draw_row(x, y):
#     timmy.penup()
#     timmy.goto(x, y)
#     timmy.pendown()
#     for _ in range(10):
#         timmy.color(rn.choice(color_list))
#         timmy.forward(0)
#         timmy.penup()
#         timmy.forward(50)
#         timmy.pendown()
#
# y = -235
# for _ in range(10):
#     x = -240
#     draw_row(x,y)
#     y += 50
#

timmy.speed("fastest")
timmy.hideturtle()

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100



for dot_count in range(1, number_of_dots + 1):

    timmy.dot(20, rn.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


timmy.pendown()

screen = t.Screen()
screen.exitonclick()
