import pandas

data = pandas.read_csv('NATO_phonetic_alphabet.csv')

phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = list(input('Enter a Word: ').upper())
    try:
        alphabet_list = [phonetic_alphabet[key] for key in user_input]
    except KeyError:
        print("Please Enter only word in alphabet.")
        generate_phonetic()
    else:
        print(alphabet_list)


generate_phonetic()
