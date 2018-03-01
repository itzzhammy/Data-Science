import pandas as pd
import matplotlib.pyplot as plt
dataset= pd.read_csv("C:/Users/Hamza/Desktop/Datasets/Datasets/gapminder.csv")
year= dataset["year"]
life_exp= dataset["life_exp"]
population= dataset["population"]
gdp_cap= dataset ["gdp_cap"]

#3
#It would make straight line as gdp_cap is on X axis .
plt.plot(gdp_cap,life_exp)
plt.show()
