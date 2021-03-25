# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day!")
#     print("Drink plenty of water.")
# elif is_cold:
#     print("It's a cold day!")
#     print("Wear warm clothes.")
# else:
#     print("It's a lovely day")
# print("Enjoy your day!")

print('''          Activity
Price of a house is $1M.
If buyer has good credit,
they need to put down 100%
Otherwise
they need to put down 20%
Print the down payment
*********************************''')

is_goodCredit = True
price = 1000000
if is_goodCredit:
    down_payment = price * .1
else:
    down_payment = price * .2
print(f'Down payment = ${down_payment}')