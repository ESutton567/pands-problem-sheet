# This program calculates BMI (kg/m2)
# Author: Éilis Sutton
# Reference 1: I copied your addOne.py program instructions
# Reference 2: Me - I know the formula for BMI

# We must convert the string that input returns to an int
# Height must be input as cm as decimal point numbers (kg value) cannot be computed to base 10 (Figured this out through an error I received)
# Height must also be converted to kg in the program as the formula requires it in this format
weight = int(input("Please enter your weight (kg):"))
height = int(input("Please enter your height (cm):"))
newNumber = weight/((height/100)**2)
print('The BMI is kg/m2: {}' .format (newNumber))