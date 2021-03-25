class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return "{name} Located at: {franchise}".format(name=self.name, franchise=self.franchises)

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def available_menus(self, time):
        menu = []
        for available_menu in menus:
            if time >= available_menu.start_time and time <= available_menu.end_time:
                menu.append(available_menu)
        return menu

    def __repr__(self):
        return "{address}".format(address=self.address)

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} is available from {start} - {end}".format(name=self.name, start=self.start_time, end=self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill

#Basta Fazoolin Business
#Brunch
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

#Early Bird
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)

#Dinner
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

#Kiddie Meal
kid_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kid_menu = Menu("Kiddie Meals", kid_items, 1100, 2100)

menus = [brunch_menu, early_bird_menu, kid_menu, dinner_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment_store = Franchise("12 East Mulberry Street", menus)

basta_fazoolin_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment_store])

#Arepa Business

arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa_menu = Menu("Arepa Menu", arepa_items, 1000, 2000)
arepa_store = Franchise("189 Fitzgerald Avenue", arepa_menu)
arepa_business = Business("Take a' Arepa", [arepa_store])

print(arepa_store.menus)
