from matplotlib import pyplot as plt


days = range(7)
money_spent = [10, 12, 12, 10, 14, 22, 24]

print(days)
print(money_spent)
plt.plot(days, money_spent)
plt.show()