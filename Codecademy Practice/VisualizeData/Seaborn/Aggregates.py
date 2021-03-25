# import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

gradebook = pd.DataFrame([
    [0 ,'Amy', 'Assignment 1', 75],
    [1, 'Amy', 'Assignment 2', 82],
    [2, 'Bob', 'Assignment 1', 99],
    [3, 'Bob', 'Assignment 2', 90],
    [4, 'Chris', 'Assignment 1', 72],
    [5, 'Chris', 'Assignment 2', 66],
    [6, 'Dan', 'Assignment 1', 88],
    [7, 'Dan', 'Assignment 2', 82],
    [8, 'Ellie', 'Assignment 1', 91],
    [9, 'Ellie', 'Assignment 2', 85]
],
    columns=['ID', 'Name', 'Assignment_Number', 'Grade']
)
print(gradebook)

assignment1 = gradebook[gradebook.Assignment_Number == 'Assignment 1']
print(assignment1)

asn1_median = np.median(assignment1.Grade)
print(asn1_median)

sns.barplot(data=gradebook,
  x=gradebook.Assignment_Number,
  y=gradebook.Grade)

plt.show()



#
# gradebook = pd.read_csv("gradebook.csv")
#
# sns.barplot(data=gradebook,
#   x=gradebook.assignment_name,
#   y=gradebook.grade)
#
# plt.show()
