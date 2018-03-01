import matplotlib.pyplot as plt
import pandas as pd
#1
dataset= pd.read_csv("C:/Users/Hamza/Desktop/Datasets/Datasets/gapminder.csv")
year= dataset["year"]
life_exp= dataset["life_exp"]
population= dataset["population"]
gdp_cap= dataset ["gdp_cap"]


#5
#For 5 bins
plt.hist(life_exp, bins = 5)
plt.show()
plt.clf()

#20 bins
plt.hist(life_exp, bins = 20)
plt.show()
plt.clf()

#20 bins show better results