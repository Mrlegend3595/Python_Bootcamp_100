from turtle import Screen, Turtle

def move_forward():
    timmy.forward(100)

timmy = Turtle()
screen = Screen()



screen.listen()
#Higher order function
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()