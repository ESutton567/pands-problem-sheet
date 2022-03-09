# This program takes a floating point number as input and 
# outputs an approximation of it's square root
# Ref 1: https://www.adamsmith.haus/python/answers/how-to-calculate-a-square-root-in-python
# Ref 2: https://stackoverflow.com/questions/1623375/writing-your-own-square-root-function
# Ref 3: https://www.youtube.com/watch?v=3i9KozCUKU4

# Create a function called sqrt that does this


num1 = float(input("Please enter a positive number: "))

# Use Newton's method to write a square root algorithm
def sqrt(y: float) -> float:
    x: float = y
    for _ in range (0,6):          # This repeats the instruction on line below (6 repeats seem to be fairly accurate)
        x = x - (x * x - y) / (2 * x)   # Asking: x^2 - y = 0 (y [slope] is a known constant)
    return x            # Call the function

# Need to define x here again as it is only defined within the function above
ans = sqrt(num1)          # Make sure to include the whole function name here
print ("The square root of 14.5 is approx {} ".format (ans)) 
    



