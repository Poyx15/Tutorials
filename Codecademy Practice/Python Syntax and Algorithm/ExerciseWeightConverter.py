weight = input("Enter your weight: ")
kilo_pounds = input("Is it (k)g or (l)bs? ")

if kilo_pounds.upper() == "K":
    print('Your weight on Lbs is ', int(weight) * 2.2)
elif kilo_pounds.upper() == "L":
    print('Your weight on Kilo', int(weight) / 2.2)
else:
    print("Wrong input")
