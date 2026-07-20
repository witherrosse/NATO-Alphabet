import pandas



data = pandas.read_csv('nato_phonetic_alphabet.csv')



letters_list = str(data.letter.to_list())
code_list = str(data.code.to_list())



phonetic = {
    row.letter: row.code for (index, row) in data.iterrows()
}



def generate():
    ''' convert name to NATO phonetic codes '''

    user_input = input("Enter your name : \n").upper()

    try:


        

        name_list = [phonetic[letter] for letter in user_input]

    except KeyError:

        


        print(" Sorry, you have to enter your name .  Numbers and symbols are not valid :D")

        generate()   

    else:


        

        print(name_list)



generate()
