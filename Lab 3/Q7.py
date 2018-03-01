import pandas as pd
import matplotlib.pyplot as plt

dataset= pd.read_csv("C:/Users/Hamza/Desktop/Datasets/Datasets/gapminder.csv")
year= dataset["year"]
life_exp= dataset["life_exp"]
population= dataset["population"]
gdp_cap= dataset ["gdp_cap"]

#7
#dictionary
europe = {'Spain':'Madrid', 'France':'Paris', 'Germany':'Bonn', 
          'Norway':'Oslo', 'Italy':'Rome', 'Poland':'Warsaw', 'Australia':'Vienna' }
#iterating the values
for key, value in europe.items() :
     print("The Capital of " + str(key) + " is " + str(value))
     