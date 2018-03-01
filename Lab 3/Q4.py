import pandas as pd
import matplotlib.pyplot as plt

dataset= pd.read_csv("C:/Users/Hamza/Desktop/Datasets/Datasets/gapminder.csv")
year= dataset["year"]
life_exp= dataset["life_exp"]
population= dataset["population"]
gdp_cap= dataset ["gdp_cap"]
#4 
#As given data is already in Year=2007 and is of Differet Countries
#so we just have to implement logarithmic scale
plt.scatter(gdp_cap,life_exp)
plt.xscale('log')
plt.show()