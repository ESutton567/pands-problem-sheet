# This program asks the user to input a string and outputs every second letter in reverse order
# Author: Éilis Sutton

# To retrieve every other character of the input sentance from index 0 (0 being the first character) to the end -> [::2] 
# Ref: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python

# To retrieve these characters in reverse order add a minus in to [::2] -> [::-2] 
# Ref: https://realpython.com/reverse-string-python/


message = input("Please enter a sentance: ")[::-2] 
print(message)

