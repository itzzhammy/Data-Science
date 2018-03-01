import pandas as pd
#8
#car.csv
cars_dataset= pd.read_csv("C:/Users/Hamza/Desktop/Datasets/Datasets/cars.csv",index_col=0)
cars_per_cap= cars_dataset["cars_per_cap"]
country= cars_dataset["country"]
drives_right= cars_dataset["drives_right"]

for lab, row in cars_dataset.iterrows() :
    print(lab)
    print(row)