# This program calculates BMI (kg/m2)
# Author: Éilis Sutton
# Reference 1: I copied your addOne.py program instructions
# Reference 2: Me - I know the formula for BMI

# We must convert the string that input returns to an int
# Height must be input as cm as decimal point numbers (kg value) cannot be computed to base 10 (Figured this out through an error I received)
# Height must also be converted to kg in the program as the formula requires it in this format

# asks the user to input their weight
weight = int(input("Please enter your weight (kg):"))
# asks the user to input their height
height = int(input("Please enter your height (cm):"))
# creates a variable that calculates BMI as per the formula
newNumber = weight/((height/100)**2)
# outputs the variable based on the user input
print('The BMI is kg/m2: {}' .format (newNumber))