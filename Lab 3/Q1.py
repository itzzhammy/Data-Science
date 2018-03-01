import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

brics= pd.read_csv("C:/Users/k153619/Desktop/Lab 3/Datasets/cars.csv")
dataset=pd.read_csv("C:/Users/k153619/Desktop/Lab 3/Datasets/gapminder.csv")
year= dataset["year"]
life_exp= dataset["life_exp"]
population= dataset["population"]
gdp_cap= dataset ["gdp_cap"]
country= dataset["country"]
#plt.scatter(year,life_exp)
#plt.hist(year,bins= 3)
#plt.show()
#for i in range(10):
 #   print(np.len(country))
 
# dic=['a':65,'b':66,'c':67]
#print(dic['a'])
# fam=[1.73,1.68,1.71,1.89]
# for index,height in enumerate(fam):
#     print("index" +str(index) +":" +str(height))