import inflect

p = inflect.engine()


def convert_number(text):
    temp_str = text.split()
    new_string = []

    for word in temp_str:
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)

    temp_str = ' '.join(new_string)
    return temp_str
