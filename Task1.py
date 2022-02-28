import string


# function for getting number of characters in a string
def get_num_of_characters(characters):
    amount = 0
    for num in characters:
        amount += 1
    return amount


# function to remove spaces and tabs from a string
def output_without_whitespace(characters):
    i = 0
    while i < len(characters):
        if characters[i] == " " or characters[i] == "\t":
            # changes character string to keep whatever is on the left of the current index that has the space or tab
            # and index gets replaced by element next to it
            characters = characters[:i] + characters[i + 1:]
        else:
            i += 1
    return characters


# function to turn a phrase into an acronym
def get_acronym(characters):
    # -----------------original code but did not work if there were multiple " " or \t-----#
    # add first letter
    # acronym = characters[0]

    # iterate over string
    # for i in range(1, len(characters)):
    # if characters[i - 1] == ' ' or characters[i - 1] == '\t':
    # add letter next to space
    # acronym += characters[i]
    # ---------------end original code---------------------------------------------------#

    # takes first letter of each word after being split by spaces tab or newlines into a list
    acronym = [char[0] for char in characters.split()]

    # concatenates all the letters from the acronym list and makes it uppercase
    return "".join(acronym).upper()


# function to encrypt messages
def get_safe(message, key):
    # gets lower and upper case alphabet letter into a string
    lower_case = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    upper_case = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # initializing variable
    encrypted_message = ""

    # iterates through every character in message
    for char in message:
        if char in lower_case:  # checks if character is in the letters list
            char_index = lower_case.find(char)  # gets index of alphabet that matches the character
            encrypted_message += key[char_index]    # assigns key element in place of the alphabet into new message
        elif char in upper_case:
            char_index = upper_case.find(char)  # gets index of alphabet that matches the character
            # assigns key element in place of the alphabet into new message but in uppercase
            encrypted_message += key[char_index].upper()
        else:
            encrypted_message += char   # if not a letter then char stays the same in the encrypted message

    return encrypted_message


def main():
    # Ask input from user to initialize functions
    user_input = input("\n\nHello please enter a word or sentence: \n")
    print("You inputted: \"{}\"".format(user_input))
    # returns num of characters
    print("There are", get_num_of_characters(user_input), "characters in the text you inputted")
    # returns input without whitespace
    print("This is your input without spaces or tabs:", output_without_whitespace(user_input))

    # ask user for a new phrase and returns acronym made from phrase
    phrase = input("\nEnter a new phrase: \n")
    print("This is your new phrase as an acronym:", get_acronym(phrase))

    # ask user for a message they want to encrypt and a key to encrypt it with
    print("\nNow let us do some encryptions")
    message = input("Please input the word or sentence you would like to be encrypted: \n")
    key = input("Please input what you would like your key to be: \n")
    # returns encrypted message
    print("This is your encrypted phrase: ", get_safe(message, key))
