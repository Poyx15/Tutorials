
from matplotlib import pyplot as plt
import random
# Add your code below:
numbers_a = range(1,13)
numbers_b = []

for rnd in numbers_a:
  numbers_b.append(random.randint(0,1001))

plt.plot(numbers_a, numbers_b)
plt.show()