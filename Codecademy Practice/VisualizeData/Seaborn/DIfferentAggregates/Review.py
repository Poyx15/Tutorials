# To review the seaborn workflow:


# 1. Ingest data from a CSV file to Pandas DataFrame.
# df = pd.read_csv('file_name.csv')

# 2. Set sns.barplot() with desired values for x, y, and set data equal to your DataFrame.
# sns.barplot(data=df, x='X-Values', y='Y-Values')

# 3. Set desired values for estimator and hue parameters.
# sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value')

# 4. Render the plot using plt.show().
# plt.show()

# import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")

sns.barplot(data=df, x="Gender", y="Patient ID", hue="Age Range")

#sns.barplot(data=survey, x="Age Range", y="Patient ID", hue="Gender")

plt.show()