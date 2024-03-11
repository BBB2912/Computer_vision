
import pandas as pd
names=pd.read_csv('nato_phonetic_alphabet.csv')

names_dic={row.letter:row.code for (index,row) in names.iterrows()}
print(names_dic)

def generate_phonetics():
    name=input('Enter a name:').upper()
    try:
        phonetic_code_words=[f'{letter}-{names_dic[letter]}' for letter in name]
    except KeyError as error:
        print(f'{error}:Sorry, only letters in the alphabet please. ')
        generate_phonetics()
    else:
        print(phonetic_code_words)
generate_phonetics()

