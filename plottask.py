# This program displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3
# in the range [0,4] on the one set of axes
# Author: Éilis Sutton
# Ref 1: lab8.10
# Ref 2: https://www.w3schools.com/python/matplotlib_plotting.asp
# Ref 3: https://calc-again.readthedocs.io/en/latest/tutorials/01-plotting-and-functions.html
# Ref 4: https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
# Ref 5: https://www.w3schools.com/python/matplotlib_line.asp
# Ref 6: https://www.w3schools.com/python/matplotlib_labels.asp
# Ref 7: https://www.geeksforgeeks.org/matplotlib-pyplot-title-in-python/
# Ref 8: https://matplotlib.org/stable/gallery/color/named_colors.html

from re import X
import numpy as np                  # import package to work with array data
import matplotlib.pyplot as plt     # pyplot is a state-based interface to matplotlib

x = np.array([1,4])             # assign the range to the variable x (as an array)

def f(x):                       # Ref 3 - define f(x)
    return x

def g(x):
    return x * x                # we can simply multiply (to power x to 2) in this way as x an array

def h(x):
    return x ** 3               # power x to 3

# print(f(x), g(x), h(x))       # use this to test that the functions work

# Ref 4 - plot each function separately and assign colour
# Ref 5 - line style
# Ref 8 - list of colors in matplotlib
plt.plot(x, f(x), color='navy', label='f(x)')  
plt.plot(x, g(x), color='royalblue', label='g(x)', ls='--') 
plt.plot(x, h(x), color='deepskyblue', label='y(x)', ls=':')     

plt.legend()
plt.xlabel('x')
plt.ylabel('y')

# Ref 7 - titling and formating font  
plt.title(label='Functions\nf(x)=x\ng(x)=x^2\nh(x)=x^3', fontsize=12, color='midnightblue')

plt.show()                      # call a visual of the the plot



