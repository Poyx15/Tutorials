class Trainer:
    def __init__(self, name, pokemons = [], items = {}, badges = []):
        self.name = name
        self.pokemons = pokemons
        self.items = items
        self.badges = badges
        items.update({"pokeballs": 10, "elixir": 5, "gold": 100})


    def get_pokemon(self, pokemon):
        pokemons = []
        pokemons = pokemons + self.pokemons
        if type(pokemon) == Pokemon:
            pokemons.append(pokemon)
        return pokemons


    def get_items(self, items):
        if type(items) == dict:
            self.items.update(items)
        else:
            print(items + " is not a TYPE of dictionary")

    def get_badge(self, name):
        self.badges.append(name)


    def __repr__(self):
        return "Hi, I am {name} owner of {pokemons}. My badges are: {badges}".format(name=self.name, pokemons=self.pokemons, badges=self.badges)

class Pokemon:
    def __init__(self, name, evolutions, elemental_affinity, class_type, attacks, level = 1, health_points = 100):
        self.name = name
        self.evolutions = evolutions
        self.elemental_affinity = elemental_affinity
        self.class_type = class_type
        self.level = level
        self.attacks = attacks
        self.health_points = health_points

    def __repr__(self):
        return self.name

# Monsters -------------------------------------
# Bulbasaur
bulbasaur_evolutions = ["Bulbasaur", "Ivysaur", "Venusaur"]
bulbasaur_attacks = {"Tackle": 10, "Vine Whip": 45, "Seed Bomb": 80, "Solar Beam": 120}

bulbasaur = Pokemon("Bulbasaur", bulbasaur_evolutions, "Grass", "Poison", bulbasaur_attacks, 10, 180)

# Charmander
charmander_evolutions = ["Charmander", "Charmeleon", "Charizard"]
charmander_attacks = {"Scratch": 40, "Dragon Breath": 60, "Dragon Fang": 65, "Flame Thrower": 90}

charmander = Pokemon("Charmander", charmander_evolutions, "Fire", "Dragon", charmander_attacks,  8, 150)

# Squirtle
squirtle_evolutions = ["Squirtle", "Wartortle", "Blastoise"]
squirtle_attacks = {"Tackle": 40, "Water Gun": 40, "Water Pulse": 60, "Aqua Tail": 90}

squirtle = Pokemon("Squirtle", squirtle_evolutions, "Water", "Monster", squirtle_attacks, 9, 165)

# Trainers -------------------------------------
ash_ketchum = Trainer("Ash Ketchum")
dania = Trainer("Dania Agbanlog")
# dania.get_pokemon(squirtle)
poy = Trainer("Poyx15")
# dania.get_pokemon(bulbasaur)
ash_ketchum.get_pokemon(squirtle)
ash_ketchum.get_pokemon(charmander)
ash_ketchum.get_items({"rope": 1, "flash light": 1, "TM": 5})

ash_ketchum.get_badge("Kanto League")

print(ash_ketchum.get_pokemon(charmander))
print(dania)
print(poy.get_pokemon(squirtle))
print(ash_ketchum)
