# Example 2
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)

# example 2
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# Example on enumerate, this prints out the values with their respective indicies 
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    print("room " + str(index) + ": " + str(a))

# Output is, 
# <script.py> output:
    room 0: 11.25
    room 1: 18.0
    room 2: 20.0
    room 3: 10.75
    room 4: 9.5
# Example for index to start with 1,
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))

# Loop over list of lists
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")

# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")
#Output
# the hallway is 11.25 sqm
#the kitchen is 18.0 sqm
#the living room is 20.0 sqm
#the bedroom is 10.75 sqm
#the bathroom is 9.5 sqm
# WORKING WITH DICTIONARIES AND NUMPY ARRAYS
# for Dictionaries, we use a method .items()
# Example
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)

# Example with 1 and 2D numpy arrays
# Import numpy as np
import numpy as np

# For loop over np_height ( This is just one numpy array)
for height in np_height:
    print(str(height) + " inches")

# For loop over np_baseball (this is an array of 2 numpy arrays)
for baseball in np.nditer(np_baseball):
    print(baseball)

# TO LOOP WITH PANDAS DATAFRAME
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row  in cars.iterrows():
    print(lab)
    print(row)
US
cars_per_cap              809
country         United States
drives_right             True
Name: US, dtype: object
AUS
cars_per_cap          731
country         Australia
drives_right        False
Name: AUS, dtype: object
JPN
cars_per_cap      588
country         Japan
drives_right    False
Name: JPN, dtype: object
IN
cars_per_cap       18
country         India
drives_right    False
Name: IN, dtype: object
RU
cars_per_cap       200
country         Russia
drives_right      True
Name: RU, dtype: object
MOR
cars_per_cap         70
country         Morocco
drives_right       True
Name: MOR, dtype: object
EG
cars_per_cap       45
country         Egypt
drives_right     True
Name: EG, dtype: object

<script.py> output:
    US
    cars_per_cap              809
    country         United States
    drives_right             True
    Name: US, dtype: object
    AUS
    cars_per_cap          731
    country         Australia
    drives_right        False
    Name: AUS, dtype: object
    JPN
    cars_per_cap      588
    country         Japan
    drives_right    False
    Name: JPN, dtype: object
    IN
    cars_per_cap       18
    country         India
    drives_right    False
    Name: IN, dtype: object
    RU
    cars_per_cap       200
    country         Russia
    drives_right      True
    Name: RU, dtype: object
    MOR
    cars_per_cap         70
    country         Morocco
    drives_right       True
    Name: MOR, dtype: object
    EG
    cars_per_cap       45
    country         Egypt
    drives_right     True
    Name: EG, dtype: object

# Example 2 - TO SELECT VARIABLES USING SQUARE BRACKETS []
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
US: 809
AUS: 731
JPN: 588
IN: 18
RU: 200
MOR: 70
EG: 45

<script.py> output:
    US: 809
    AUS: 731
    JPN: 588
    IN: 18
    RU: 200
    MOR: 70
    EG: 45

# To add a column
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)
     cars_per_cap        country  drives_right        COUNTRY
US            809  United States          True  UNITED STATES
AUS           731      Australia         False      AUSTRALIA
JPN           588          Japan         False          JAPAN
IN             18          India         False          INDIA
RU            200         Russia          True         RUSSIA
MOR            70        Morocco          True        MOROCCO
EG             45          Egypt          True          EGYPT

<script.py> output:
         cars_per_cap        country  drives_right        COUNTRY
    US            809  United States          True  UNITED STATES
    AUS           731      Australia         False      AUSTRALIA
    JPN           588          Japan         False          JAPAN
    IN             18          India         False          INDIA
    RU            200         Russia          True         RUSSIA
    MOR            70        Morocco          True        MOROCCO
    EG             45          Egypt          True          EGYPT

# Using apply
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)