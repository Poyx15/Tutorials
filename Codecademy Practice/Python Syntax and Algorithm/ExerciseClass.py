class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}.')


person1 = Person("Poy")
person1.talk()

person2 = Person("Dania")
person2.talk()
