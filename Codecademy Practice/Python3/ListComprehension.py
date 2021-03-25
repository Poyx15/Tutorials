capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = ["{capital}, {country}".format(capital=capital, country=country) for capital, country in zip(capitals, countries)]
print(locations)

temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_adjusted = [temp + 20 for temp in temperatures]