# import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

rating = []
for i in range(100):
  rating.append(soup.select('td.Rating')[i].get_text())

plt.hist(rating, bins=25)
plt.title("First 100 rating of Cacao")
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()