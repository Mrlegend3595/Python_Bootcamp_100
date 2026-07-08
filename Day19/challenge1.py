from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()

#My Solution
# def move_forward():
#     timmy.forward(20)
#
# def clockwise():
#     timmy.right(5)
#
# def counter_clockwise():
#     timmy.left(5)
#
# def backward():
#     timmy.backward(20)
#
# def clear_drawing():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=backward)
# screen.onkey(key="a",fun=counter_clockwise)
# screen.onkey(key="d",fun=clockwise)
# screen.onkey(key="c",fun=clear_drawing)
#######################################################
def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)


screen.exitonclick()