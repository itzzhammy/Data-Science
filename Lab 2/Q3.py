import numpy as np
height= [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 71, 75, 77, 74, 73, 74, 78, 73, 75, 73]
weight= [180, 195, 195, 190, 230, 190, 200, 190, 190, 200, 200, 184, 200, 180, 219, 187, 200, 220, 205, 190, 170, 160, 215, 175, 205, 200, 214, 200, 190, 180, 205, 220, 190, 215]
np_height=np.array(height)
np_height*0.0254

np_weight=np.array(weight)

np_weight*0.453592
print(np_weight)
bmi=np_weight/np_height**2
print(bmi)