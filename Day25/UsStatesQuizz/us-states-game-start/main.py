import turtle
import pandas

# import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#My_Code
# score = 0
# correct_guess_list = []
# game_on = True
#
# while game_on:
#
#     answer_state = screen.textinput(f"{len(correct_guess_list)}/50 States Correct", "What's another state's name?").title()
#
#     with open("50_states.csv") as states_file:
#         states = csv.reader(states_file)
#         for row in states:
#             if row[0] == answer_state:
#                 correct_guess_list.append(answer_state)
#                 new_text = turtle.Turtle()
#                 new_text.hideturtle()
#                 new_text.penup()
#                 new_text.goto(float(row[1]), float(row[2]))
#                 new_text.write(row[0])
#
#
#     if len(correct_guess_list) == 50:
#         game_on = False


#Solution
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                    "What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)


        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]

        t.goto(int(state_data.x.iloc[0]) , int(state_data.y.iloc[0]))
        # t.write(state_data.state.item())
        t.write(answer_state)

