from random import randint
from replit import clear

from art import logo,vs
from data import data_list

#select two information for showing to user
def number_info():
    """return index of data from datalist"""
    index = randint(0, len(data_list) - 1)
    return index

def create_comparing():
    """return two data for comparing and game"""
    a = number_info()
    b = number_info()

    while a == b:
        b = number_info()

    return {"A":data_list[a], "B":data_list[b]}


#Comparing
def right_answer(a,b):
    """return right answer between two choices"""
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"


def game():
    """game start point in here"""

    score = 0
    score_message =""

    # repeat game while user selecting true choice
    while True:
        # print logo
        print(logo)
        print(score_message)

        # two random data select
        info = create_comparing()
        answer = right_answer(info["A"],info["B"])

        #selecting choice by user
        print(f"Compare A: {info['A']['name']}, {info['A']['description']}, from {info['A']['country']}")
        print(vs)
        print(f"Compare B: {info['B']['name']}, {info['B']['description']}, from {info['B']['country']}")
        choice = input("Who has more followers? type 'A' or 'B': ").upper()

        #result
        if choice == answer:
            score += 1
            score_message = f"You're right! Current score: {score}."
            clear()
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            #end game
            return



#my problem was replacing b_info with information for the next round.
game()