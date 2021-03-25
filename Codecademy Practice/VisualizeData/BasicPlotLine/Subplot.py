# The command plt.subplot() needs three arguments to be passed into it:
#
# The number of rows of subplots
# The number of columns of subplots
# The index of the subplot we want to create

from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1,2,1)
plt.plot(months, temperature)

# The "o" parameter stand for scattered spot
plt.subplot(1,2,2)
plt.plot(flights_to_hawaii, temperature, "o")

plt.show()