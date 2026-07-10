import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "cyan", "purple", "pink"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! the {winning_color} turtle is the winner!.")
            else:
                print(f"You've Lost! the {winning_color} turtle is the winner!.")
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


#My Solution of oop challenge2
# timmy = Turtle(shape="turtle")
# tommy = Turtle(shape="turtle")
# benny = Turtle(shape="turtle")
# alex = Turtle(shape="turtle")
# sam = Turtle(shape="turtle")
# matthew = Turtle(shape="turtle")
#
# racers = [timmy, tommy, benny, alex, sam, matthew]
#
# y=-50
# for number in range(6):
#     racers[number].color(colors[number])
#     racers[number].penup()
#     racers[number].goto(x=-230,y=y)
#     y += 30

#--------------------------------------------------

############################################################

screen.exitonclick()