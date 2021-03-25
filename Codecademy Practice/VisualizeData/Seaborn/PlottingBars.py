# The Seaborn function sns.barplot(), takes at least three keyword arguments:
#
# data: a Pandas DataFrame that contains the data (in this example, data=df)
# x: a string that tells Seaborn which column in the DataFrame contains otheur x-labels (in this case, x="Gender")
# y: a string that tells Seaborn which column in the DataFrame contains the heights we want to plot for each bar (in this case y="Mean Satisfaction")
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# This is the dataframe
df = pd.DataFrame([
    ['Male', 7.2],
    ['Female', 8.1],
    ['Non-binary', 6.8]

],
  columns=['Gender','Mean Satisfaction']
)
# Dataframe until here  ^^^^^^^^
print(df)

# The Magic of Seaborn
sns.barplot(
	data= df,
	x= 'Gender',
	y= 'Mean Satisfaction'
)

# Just like print() but show()
plt.show()