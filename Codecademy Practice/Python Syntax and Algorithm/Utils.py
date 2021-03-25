# numbers = [10, 3, 6, 2, 29]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum