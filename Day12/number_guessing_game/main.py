import random
from art import logo

def level_choice():
    """return level of chance for guessing"""
    level = input("Choose a Difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5

def random_number():
    """return a random number as a answer."""
    return random.randint(1, 100)


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

chance = level_choice()
answer = random_number()

while chance != 0 :
    print("You have " + str(chance) + " attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == answer:
        print("You got it! the answer is " + str(answer))
        break

    elif guess > answer:
        print("Too high!")
        chance -= 1

    else:
        print("Too low!")
        chance -= 1

    if chance == 0:
        print("You lose!")
    else:
        print("Guess again!")





