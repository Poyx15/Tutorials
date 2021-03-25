# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     for item in row:
#         print(item)

# My answer
# numbers = [5, 2, 1, 7, 4, 6, 8, 232, 67, 89, 69, 69,  4, 2, 6]
# uniques = []
# numbers.sort()
# temp = numbers[0]
# print(numbers)
# for number in numbers:
#     if number != temp:
#         uniques.append(temp)
#     temp = number
# print(uniques)

# Correct Answer
numbers = [5, 2, 1, 7, 4, 6, 8, 232, 67, 89, 69, 69,  4, 2, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
