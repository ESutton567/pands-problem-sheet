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
# Ref 9: https://stackoverflow.com/questions/18962063/matplotlib-setting-title-bold-while-using-times-new-roman
# Ref 10 :https://www.tutorialspoint.com/how-to-write-text-in-subscript-in-the-axis-labels-and-the-legend-using-matplotlib
# Ref 11: https://python-graph-gallery.com/web-line-chart-with-labels-at-line-end

from tkinter.font import BOLD
from matplotlib.font_manager import FontProperties
import numpy as np                  # import package to work with array data
import matplotlib.pyplot as plt     # pyplot is a state-based interface to matplotlib
from matplotlib import rc

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
# Ref 10: using subscript text
plt.plot(x, f(x), color='navy', label='f(x) = x')  
plt.plot(x, g(x), color='royalblue', label=r'g(x) = $x^2$', ls='--') 
plt.plot(x, h(x), color='deepskyblue', label=r'y(x) = $x^3$', ls=':')     

plt.legend()
plt.xlabel('x',fontweight=BOLD)
plt.ylabel('y',fontweight=BOLD)

# Ref 7 - titling and formating font 
# Ref 9 - fontweight 
plt.title(
    label='Maths Functions',
    fontname='Times New Roman',
    fontsize=14, 
    fontweight=BOLD
    )

# Ref 11 - customise text
plt.text(
    2.5, 
    -11, 
    "Produced by Éilis Sutton", 
    fontname="Times New Roman", 
    fontsize=9, 
    color='black', 
    ha='center',
)

plt.show()                      # call a visual of the the plot



