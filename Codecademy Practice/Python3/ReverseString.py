# Write your reverse_string function here:
def reverse_string(word):
    temp = []
    temp2 = []
    for letter in word:
        temp.append(letter)

    for index in range(len(temp)):
        temp2.append(temp[-index -1])

    pmet = ""

    for letter in temp2:
        pmet = pmet + letter

    return pmet


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print