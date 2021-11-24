"""
    program that returns the phonetic spelling of a word
    for example angela returns ['Alfa', 'November', 'Golf', 'Echo', 'Lima', 'Alfa']
    like a as in alpha, n as in november ...
    uses pandas and list and dictionary comprehension
"""
import pandas

phonetic_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

#  Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for index, row in phonetic_alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word: ').upper()
result = [phonetic_dict[item] for item in user_input]
print(result)
