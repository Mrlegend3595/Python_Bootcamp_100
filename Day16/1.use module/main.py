#use module
# import another_module
# print(another_module.another_variable)

# import turtle
from turtle import Turtle ,Screen


# timmy = turtle.Turtle()
timmy = Turtle()

# print(timmy) #output: <turtle.Turtle object at {Address in your computer}>

timmy.shape("turtle")

# challenge: change color of timmy to green
#methode color
timmy.color("green")

#Challenge: move turtle
timmy.forward(100)

#my_screen = turtle.Screen()
my_screen = Screen()



print(my_screen.canvheight)

my_screen.exitonclick()








