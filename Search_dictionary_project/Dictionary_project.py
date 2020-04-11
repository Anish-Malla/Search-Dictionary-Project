import json
import difflib

dictionary_data = json.load(open("data.json"))

def input_word():
    while True:
        try:
            word = str(input("What word's meaning do you want: "))
        except TypeError:
            print("Please do not include any numbers or special characters")
        return word

def getting_meaning(word):

    if word.title() in dictionary_data:
        return dictionary_data.get(word)
    elif word.upper() in dictionary_data:
        return dictionary_data.get(word)
    elif word.lower() in dictionary_data:
        return dictionary_data.get(word)
    elif len(difflib.get_close_matches(word, dictionary_data.keys())) > 0:
        guess_word = input(f"Did you mean to say any of the below word / words (yes or no): \n{difflib.get_close_matches(word, dictionary_data.keys())}\n: ")
        if guess_word.lower()[0] == "y":
            # if len(difflib.get_close_matches(word, dictionary_data.keys())) >= 2 :
            choice = int(input("choose which word's meaning u want (for the first word type 1 and for the second word type 2 and so on... )"))
            return dictionary_data.get(difflib.get_close_matches(word, dictionary_data.keys())[choice - 1])
            # elif len(difflib.get_close_matches(word, dictionary_data.keys())) == 1 and guess_word.lower()[0] == "y":
            #     return dictionary_data.get(difflib.get_close_matches(word, dictionary_data.keys()))[0]
    else:
        pass

run = True
while run == True:
    search_word = input_word()
    print(getting_meaning(search_word))

    again = input("Do you want to search the meaning of another word? (yes or no) ")

    if again.lower()[0] == "y":
        run = True
    else:
        run = False
# a change has been made
