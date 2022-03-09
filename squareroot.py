# This program takes a floating point number as input and 
# outputs an approximation of it's square root
# Reference 1: https://www.adamsmith.haus/python/answers/how-to-calculate-a-square-root-in-python


# Create a function called sqrt that does this

num1 = float(input("Please enter a positive number: "))

def sqrt(num1):
    x = num1 ** 0.5     # Ref 1 - how to type out square root in pyhton without using a function or module
    return x            # Call the function

# Need to define x here again as it is only defined within the function above
x = sqrt(num1)          # Make sure to include the whole function name here
print ("The square root of 14.5 is approx {} ".format (x)) 
    



