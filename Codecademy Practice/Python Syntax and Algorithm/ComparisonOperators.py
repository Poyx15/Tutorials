print('''Create a program that:
if temperature is greater than 30
    it's hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold
************************************''')

temperature = 25

if temperature > 30:
    print("It is a hot day!")
elif temperature < 10:
    print("It is a cold day!")
else:
    print("It is a lovely day!")

print('''Activity:
if name is less than 3 characters long
    print "name must be at least 3 characters"
otherwise if it's more than 50 characters long
    print "name can be a maximum of 50 characters long"
otherwise
    print "name looks good
********************************************************"''')

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("name can't exceed 50 characters.")
else:
    print("Name looks good!")
