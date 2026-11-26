# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt

#NB gdp_cap, pop, life_exp - are defined lists somewhere else. For other examples, you can declare your own values
# for this example, image #1 and #2 are the results after plotting
# in this example, for me to make calculations on the data, I had to first make it an array using numpy library and to plot and customise it, I had to use matplot lib functions

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

# EXAMPLE 2 OF CUSTOMISATION
# Here we add colors as shown in photo #3
# Specify c and alpha inside plt.scatter()
# A list of colors, col with corresponding continents, a list of continents, continent- Note that these 2 lists are defined somewhere, for other examples, you can define your own colors
# And a dictionary with  a continent and its color are used
# alpha argument specifies opacity from 0 to 1, c is color
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col, alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()


# To add grids and names to data sets
# As shown by photo 4
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()