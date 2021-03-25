import random


class Dice:
    def roll(self):
        first_die = random.randint(1,6)
        second_die = random.randint(1,6)
        print(f'({first_die}, {second_die})')


dice = Dice()
dice.roll()