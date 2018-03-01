import pandas as pd

cars_dataset= pd.read_csv("C:/Users/Hamza/Desktop/Datasets/Datasets/cars.csv",index_col=0)
cars_per_cap= cars_dataset["cars_per_cap"]
country= cars_dataset["country"]
drives_right= cars_dataset["drives_right"]

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr= [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
#a
my_dict = { "country":names, 
          "drives_right":dr,
          "cars_per_cap":cpc }
#b
for key,value in my_dict.items() :
     print("Country " + str(country) + " Car_per_cap " + str(cpc) +"drives right"+str(dr))
#c
index=['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
for key,value in my_dict.items() :
     print("Index" +str(index) +"The Capital of " + str(country) + " is " + str(cpc) +"drives right"+str(dr))

#d
  car= np.array(cars_dataset)
lst = []
for i,j in enumerate(cars_dataset):
   ## print(cars[i][0])
    lst= [car[i][0] for i,j in enumerate(car) if car[i][0] >500]
lst  
#e

    lst = []
for i,j in enumerate(cars_dataset):
   ## print(cars_dataset[i][0])
   #instead of np.logical_and
   #simple and , or
    lst= [car[i][0] for i,j in enumerate(car) if car[i][0] >100 and car[i][0] <500]
lst  