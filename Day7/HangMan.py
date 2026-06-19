from replit import clear
import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)

lives = 6

chosen_word = random.choice(word_list)

display = []

word_length = len(chosen_word)

for _ in range(word_length):
    # display.append('_')
    display += '_'
# display = ['_'] * len(chosen_word)

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You have already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Sorry, you guessed {guess}. It is not in the word. you lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("you win!")

    print(stages[lives])