import pandas as pd
from matplotlib import pyplot as plt
# Add your code here
# df = pd.read_csv('time_series_covid19_confirmed_global.csv')

# df = pd.read_csv('global_population.csv')


plt.xlabel("Stock Exchange Days for Past Year")
plt.ylabel("Price")

plt.plot(business_days, open)
plt.plot(business_days, close)
plt.title("Netflix Stock Prices for past Year")
# Add your code here:
ax = plt.subplot()
ax.set_xticks([0,50,100,150,200,250])
month_names = ["Feb 2017", "Apr 2017", "Jun 2017", "Aug 2018","Oct 2018", "Dec 2017"]
ax.set_xticklabels(month_names)


print(df)
