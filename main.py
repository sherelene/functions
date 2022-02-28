from Task1 import *


if __name__ == '__main__':
    user_input = input("Hello please enter a word or sentence: \n")
    print("There are", get_num_of_characters(user_input), "characters in the text you inputted")
    print("This is your input without spaces or tabs:", output_without_whitespace(user_input))
    print("This is your input as an acronym:", get_acronym(user_input))

    print("\n Now let us do some encryptions")
    phrase = input("Please input the word or sentence you would like to be encrypted: \n")
    key = input("Please input what you would like your key to be: \n")
    print("This is your encrypted phrase: ", get_safe(phrase, key))

