# import codecademylib
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

y_lower = [rev * 0.9 for rev in revenue]
y_upper = [rev * 1.1 for rev in revenue]

#your work here
plt.plot(months, revenue)
ax = plt.subplot()
ax.set_xticks(range(len(month_names)))
ax.set_xticklabels(month_names)
plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()