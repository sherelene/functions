from Task1 import *


if __name__ == '__main__':
    user_input = input("Hello please enter a word or sentence: \n")
    print("There are", get_num_of_characters(user_input), "characters in the text you inputted")
    print("This is your input without spaces or tabs:", output_without_whitespace(user_input))
    print("This is your input as an acronym:", get_acronym(user_input))

