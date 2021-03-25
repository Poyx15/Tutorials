digit_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",o
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
# # MY answer
# phone_number = input("Enter phone number: ")
# count = 0
# temp = ""
# num = ""
# while count < len(phone_number):
#     temp = digit_mapping.get(phone_number[count])
#     num = num + temp + " "
#     count = count + 1
# print(num)

phone_number = input("Enter phone number: ")
output = ""
for ch in phone_number:
    output += digit_mapping.get(ch, "!") + " "
print(output)
