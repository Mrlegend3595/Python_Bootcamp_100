from art import logo,vs
from data import data_list
import random
from replit import clear
def format_data(account):
    """format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take the user guess and follower count and returns if they got it right."""

    #methode1: Long command
    #if a_followers > b_followers and guess == 'a':

    #methode 2
    # if a_followers > b_followers:
    #     if guess == 'a':
    #         return True
    #     else:
    #         return False

    #easier methode 3:
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


#Display art
print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data_list)


#Make the game repeatable.
while game_should_continue:

    # generate a random account from the game data.
    # making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data_list)

    while account_a == account_b:
        account_b = random.choice(data_list)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #check if user is correct
    ## get follower count of each account.
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    #Clear the screen between rounds.
    clear()
    print(logo)
    #give user feedback on their guess.
    if is_correct:
        #score keeping.
        score += 1
        print("You're right! Current score is: ",score)
    else:
        game_should_continue = False
        print("Sorry, that's wrong. Final score is: ",score)



