from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """cheks answer against guess. returns the number of turns """
    if guess == answer:
        print(f"You got it! the answer is {answer}")
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print("Too high!")
        return turns - 1


#make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        #global turns
        # turns = EASY_LEVEL_TURNS
        return EASY_LEVEL_TURNS
    else:
        # turns = HARD_LEVEL_TURNS
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"pssst, the correct answer is {answer}")

    turns = set_difficulty()

    #repeat the guessing functionality if they get it wrong.

    guess = 0
    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess the number
        guess = int(input("Make a guess: "))
        #track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer,turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()