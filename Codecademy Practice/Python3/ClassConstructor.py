class Circle:
    pi = 3.14   # You can use this variable with the command self.pi

    def __init__(self, diameter):   # Constructor
        self.radius = diameter / 2  # Assign parameter to be divided by 2 and pass it to the self.radius

    def __repr__(self):  # Force the instances to return a readable value of string.
        return "Circle with radius {radius}".format(radius=self.radius)     # self.radius camefrom the above constructor

    def area(self):     # A method in a class always have a parameter self. Multiple parameter is still possible
        return self.pi * self.radius ** 2   # self.radius is the class variable and self radius came from __init__ class

    def circumference(self):
        return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.area())
print(round_room)
