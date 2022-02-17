# This program asks the user to input any positive integer and outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Author: Éilis Sutton
# Ref: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

number = int(input("Please enter a positive integer: "))

while number != 1:
    if number % 2 == 0:                             # If the number is even
        result = number // 2                        # Print the number divided by 2
    else: 
        if number % 2 == 1:                           # If the number is odd
            result = ((3*number) +1)                    # Print the number multipled by 3 first then add 1 to this
        number = result
        
       

#def collatz(number):

#    if number % 2 == 0:                             # If the number is even
#        result = number // 2                        # Print the number divided by 2
#    elif number % 2 == 1:                           # If the number is odd
#        result = ((3*number) +1)                    # Print the number multipled by 3 first then add 1 to this
#        print (result)
#        return result                               # Rerun the program using the answer
#    while result != 1:
#        print (result)                              # This allows the program to continue running
#        number = result 
#        return result         
        
        
        
#number = int(input("Please enter an integer: "))

#def collatz(number):
#
#    if number % 2 == 0:                             # If the number is even
#        result = number // 2                        # Print the number divided by 2
#    elif number % 2 == 1:                           # If the number is odd
#        result = ((3*number) +1)                    # Print the number multipled by 3 first then add 1 to this
#        print (result)
#        return result                               # Rerun the program using the answer
#    while result != 1:
#        print (result)                              # This allows the program to continue running
#        number = result                             # This tell the program that collatz loops with the resulting number



 