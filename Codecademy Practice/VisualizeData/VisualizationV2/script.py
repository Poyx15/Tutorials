from matplotlib import pyplot as plt

# Location String	Location Code
# 'best'	            0
# 'upper right'	        1
# 'upper left'	        2
# 'lower left'	        3
# 'lower right'	        4
# 'right'	            5
# 'center left'	        6
# 'center right'	    7
# 'lower center'	    8
# 'upper center'	    9
# 'center'	            10

deaths_venomous_spider = [6,5,5,10,8,14,10,4,8,5,6]

letters_spelling_bee = [9,8,11,12,11,13,12,9,9,7,9]

years=[1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]

plt.xlabel("Year")
plt.ylabel("Total Count")

plt.plot(years, letters_spelling_bee)
plt.plot(years, deaths_venomous_spider)
plt.title("Letters in the Winning Spelling Bee Word vs. Deaths by Venomous Spider")
legend_labels = ["Letters in Winning Word", "Deaths by Venomous Spider"]
plt.legend(legend_labels, loc=0)
plt.show()
