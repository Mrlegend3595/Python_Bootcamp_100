import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
print(phonetic_dict)

#my solution
# is_valid = False
#
# while not is_valid:
#     try:
#         input_word = input("Enter a word: ").upper()
#         phonetic_code_list = [phonetic_dict[letter] for letter in input_word]
#     except KeyError:
#         print("Sorry, only letters a-z are allowed.")
#     else:
#         is_valid = True
#         print(phonetic_code_list)

def generate_phonetic():

    input_word = input("Enter a word: ").upper()
    try:
        phonetic_code_list = [phonetic_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters a-z are allowed.")
        generate_phonetic()
    else:
        print(phonetic_code_list)


generate_phonetic()