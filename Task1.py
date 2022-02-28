import string
import math


def main():
    user_input = input("Hello please enter a word or sentence: \n")
    print("You inputted: \"{}\"".format(user_input))
    print("There are", get_num_of_characters(user_input), "characters in the text you inputted")
    print("This is your input without spaces or tabs:", output_without_whitespace(user_input))

    phrase = input("\nEnter a new phrase: \n")
    print("This is your new phrase as an acronym:", get_acronym(phrase))

    print("\nNow let us do some encryptions")
    message = input("Please input the word or sentence you would like to be encrypted: \n")
    key = input("Please input what you would like your key to be: \n")
    print("This is your encrypted phrase: ", get_safe(message, key))

def get_num_of_characters(characters):
    amount = 0
    for num in characters:
        amount += 1
    return amount


def output_without_whitespace(characters):
    i = 0
    while i < len(characters):
        if characters[i] == " " or characters[i] == "\t":
            characters = characters[:i] + characters[i + 1:]
        else:
            i += 1
    return characters


def get_acronym(characters):
    #-----------------original code but did not work if there were multiple " " or \t-----#
    # add first letter
    #acronym = characters[0]

    # iterate over string
    #for i in range(1, len(characters)):
       # if characters[i - 1] == ' ' or characters[i - 1] == '\t':
            # add letter next to space
           # acronym += characters[i]
    #---------------end original code---------------------------------------------------#
    acronym = [char[0] for char in characters.split()]

    return "".join(acronym).upper()


def get_safe(message, key):
    letters = string.ascii_letters
    encrypted_message = ""
    next_index = 0
    for char in message:
        if char in letters:
            char_index = letters.find(char)
            char_index_copy = char_index

            sub_index = (5 * char_index + 17) % len(key)

            while sub_index >= len(key):
                sub_index % len(key)

            if char_index_copy >= len(key):
                encrypted_message += letters[sub_index*2]
            else:
                encrypted_message += letters[sub_index]
            next_index += 1

    return encrypted_message



