
def get_num_of_characters(characters):
    amount = 0
    for num in characters:
        amount +=1
    return amount


def output_without_whitespace(alphanum):
    i = 0
    while i < len(alphanum):
        if alphanum[i] == " " or alphanum[i] == "\t":
            alphanum = alphanum[:i] + alphanum[i + 1:]
        else:
            i += 1
    return alphanum


#def get_acronym(acronym):


#def get_safe(sentence, key):


