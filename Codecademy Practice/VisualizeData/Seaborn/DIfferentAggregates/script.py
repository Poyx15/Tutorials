# import codecademylib3_seaborn
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")
print(df)
sns.barplot(x='Gender', y='Response', data=df, estimator=len)

plt.show()

# sns.barplot(x='Gender', y='Response', data=df, estimator=np.median)
# plt.show()