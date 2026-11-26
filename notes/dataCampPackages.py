# Using Numpy
import numpy
numpy.array([1,2,3])

import numpy as np
np.array([1,2,3])

# Below is a complete example
from numpy import array
array([1,2,3])

fam =['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam_ext = fam + ['me', 1.79]
print(str(len(fam_ext))+ "elements in fam_ext") 

# Other ways of using numply
np_fam = array(fam_ext)
np_fam = np.array(fam_ext)

#MATH package
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Numpy example on heights

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_height = np.array(height)
np_weight = np.array(weight)
print(np_height)
print(np_weight)
bmi = np_weight/np_height**2

print(bmi)

#Note that python lists and numpy arrays behave differently
# You can work with numpy arrays the same way you do with lists
print(bmi[1])
# Incase you want to print bmi values greater than 23 with boolean
print(bmi > 23)
# to print only values greater than 23
print(bmi[bmi>23])

# Example on indexing in numpy
import numpy as np

np_weight_lb = np.array(weight)
np_height_in = np.array(height)

# Print out the weight at index 50
print(np_weight_lb[1])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

