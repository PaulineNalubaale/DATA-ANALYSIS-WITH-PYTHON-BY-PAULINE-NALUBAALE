import numpy as np
from numpy import array

ht_wt = [[1.73, 1.68, 1.71, 1.89, 1.79], 
         [65.4, 59.2, 63.6, 88.4, 68.7]]
# ht_wt is [0 firstrow, 1-second row]
nd_2d = np.array(ht_wt) 
print(nd_2d)
# in ht_wt we have 2 rows and 5 coluns, incase you want to call a value in the array eg below
print(nd_2d[0][2])

print(nd_2d[0, 2])
# Incase you want to select height and weight of the second and third family member
print(nd_2d[:, 1:3])

# to print all weights
print(nd_2d[1, :])