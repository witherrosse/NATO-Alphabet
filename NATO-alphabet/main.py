import pandas

### Read the NATO phonetic alphabet CSV file ###

data = pandas.read_csv('nato_phonetic_alphabet.csv')

### Get lists of letters and codes (converted to string for display) ###

letters_list = str(data.letter.to_list())
code_list = str(data.code.to_list())

### Create a dictionary mapping letters to their NATO code words ###

phonetic = {
    row.letter: row.code for (index, row) in data.iterrows()
}

### Main function to convert name to NATO phonetic codes ###

def generate():

    user_input = input("Enter your name : \n").upper()

    try:


        ### Convert each letter to its NATO code word ###

        name_list = [phonetic[letter] for letter in user_input]

    except KeyError:

        ### Handle invalid input (numbers or symbols) ###


        print(" Sorry, you have to enter your name .  Numbers and symbols are not valid :D")

        generate()   # Ask for input again

    else:


        ### Print the NATO code words for the name ###

        print(name_list)

### Start the program ###

generate()