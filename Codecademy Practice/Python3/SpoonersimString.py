def add_exclamation(word):
    temp = ""
    while len(word) + len(temp) < 20:
        temp = temp + "!"

    return word+temp


print(len(add_exclamation('yello')))

