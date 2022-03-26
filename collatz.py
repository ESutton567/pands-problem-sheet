# This program asks the user to input any positive integer and outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Author: Éilis Sutton
# Ref 1: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# Ref 2: https://java2blog.com/exit-program-python/

# create function for collatz conjecture (ref 1)
def collatz(number):  
    # if the argument is even                
    if number % 2 == 0: 
        # print argument value divided by 2              
        print(number // 2) 
        # call function to divide argument value by 2           
        return number // 2            
    
    # If the number is odd
    elif number % 2 == 1: 
            # print the argument multipled by 3 first then add 1 to this            
            result = ((3*number) +1)  
            # print input argument divided by 2
            print(result)             
            # call function to multiple input argument by 3, then add one
            return result             
           
numberInput = int(input("Please enter a positive integer: "))
# keep rerunning the function until the argument passed into the function equals 0
while numberInput != 1:               
    # pass the argument value into the collatz function
    numberInput = collatz(numberInput)
else: 
    numberInput == 1
    # quit the program when a specific output value returns back into the function (ref 2)
    quit()                            