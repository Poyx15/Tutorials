# import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

x_values = range(len(drinks))
plt.bar(x_values, sales)
plt.xticks(x_values, drinks)
plt.show()
