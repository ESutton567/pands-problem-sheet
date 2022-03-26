# This program asks the user to input a string and outputs every second letter in reverse order
# Author: Éilis Sutton

# Ref 1: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python
# Ref 2: https://realpython.com/reverse-string-python/


# ask the user to enter a sentance
# slice the argument to every 2nd element ([::2]; Ref 1)
# reverse the argument by adding a minus to the slide instruction (Ref 2) 
message = input("Please enter a sentance: ")[::-2] 
# print the message
print(message)

