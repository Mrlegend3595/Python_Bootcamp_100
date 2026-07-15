# 1. Create a dictionary in this format:
import pandas as pd
nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ").upper()
phonetic_code_list = [phonetic_dict[letter] for letter in input_word if letter in phonetic_dict.keys()]
print(phonetic_code_list)

