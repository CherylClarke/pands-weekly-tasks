
#Write a program called plottask.py that displays:

#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
#  
#and a plot of the function  h(x)=x3 in the range 0 to 10, 

#on the one set of axes.


#first import matplotlib

import matplotlib.pyplot as plt

import numpy as np

# Generate 1000 normally distributed values with mean=5 and std=2
data = np.random.normal(loc=5, scale=2, size=1000)

# Create x values for h(x) = x^3 from 0 to 10
x = np.linspace(0, 10, 400)
y = x ** 3

# Create a figure and axes
plt.figure(figsize=(10, 6))

# Plot histogram of the normal distribution
plt.hist(data, bins=30, alpha=0.6, color='skyblue', edgecolor='black', label='Normal Distribution')


# Plot h(x) = x^3 on the same axes
plt.plot(x, y, color='darkorange', linewidth=2, label=r'$h(x) = x^3$')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency / Function Value')
plt.title('Histogram of Normal Distribution and Plot of h(x) = x^3')

# Add legend
plt.legend()

# Show grid for clarity
plt.grid(True)

# Display the plot
plt.show()

#Reference : chatgpt prompt-explain histogram, https://chatgpt.com/c/680e9760-9ad4-8003-aaed-30d317cacf90

#Reference : W3schools- matplot.lib pylot , https://www.w3schools.com/python/matplotlib_pyplot.asp

# Reference : Andrew Beatty, lecture on plotting ,week 8.2









