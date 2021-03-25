# Define your functions
sizes = {
    "a" : "Small",
    "b" : "Medium",
    "c" : "Large",
    "A" : "Small",
    "B" : "Medium",
    "C" : "Large"
}


coffee_type = {
    "a" : "Brewd Coffee",
    "b" : "Mocha",
    "c" : "Latte"
}


milk_for_latte = {
    "a" : "Latte",
    "b" : "Non-fat Latte",
    "c" : "Soy Latte"
}


mocha_limited_edition = {
    "a" : "Peppermint Mocha",
    "b" : "Mocha"
}

order_drink = True
drinks_type = []
drink_size = []
drink_quantity = []

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def coffee_bot():
    print("Welcome to the cafe!")
    size = sizes.get(get_size()) #Get size

    while size == None:
        print_message()
        size = sizes.get(get_size())

    type = coffee_type.get(get_drink_type()) #Get Type

    while type == None:
        print_message()
        type = coffee_type.get(get_drink_type())

    if type == "Latte":
        milk_type = None
        while milk_type == None:
            milk_type = milk_for_latte.get(order_latte())   #Get Milk for Latte
            type = milk_type

    elif type == "Mocha":
        type = mocha_limited_edition.get(order_mocha())

    quantity_isdigit = False
    while quantity_isdigit == False:
        quantity = input("How many of this item? ")
        quantity_isdigit = quantity.isdigit()


    order = "Your Order is {} {} {}".format(quantity, size, type)
    drink_size.append(size)
    drinks_type.append(type)
    drink_quantity.append(quantity)
    print(order)

    # print(type)

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    return res


def get_drink_type():
    res = input('What type of drink do you like? \n[a] Brewd Coffee \n[b] Mocha \n[c] Latte \n> ')
    return res


def order_latte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")
    return res


def order_mocha():
    while True:
        res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>")
        if res == 'a' or res == 'b':
            return res
        print_message()


while order_drink == True:
    coffee_bot()
    res = ""
    while res != "y" or res != "n":
        res = input("Do you want to add another order? ")
        if res == "n":
            order_drink = False
            print("So to summarize everything, your orders are: ")
            drinks = list(zip(drink_quantity, drinks_type, drink_size))
            for drink in drinks:
                print(drink)
            name = input("Can I get your name please? ")
            print("Thanks, " + name + "! Your drink will be ready shortly.")
            break
        elif res == "y":
            break




