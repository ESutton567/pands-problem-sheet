# This program reads in a text file and outputs the number of e's in it
# Author: Éilis Sutton
# Ref 1: Count occurences in a text file  
# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
# Ref 2: Using the count function 
# https://www.w3schools.com/python/ref_list_count.asp
# Ref 3: Get the file from an argement on the CLI 
# https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input
# Ref 4: Moby Dick text file downloaded from 
# https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
# Ref 5: Create a function to return the letter count 
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/


import sys              # Ref 3
filename = sys.argv[-1]

def countEs(filename, letter):        # Ref 5 
    with open(filename, 'rt') as f:  # Open the file in read mode(text file)
        es = f.read()               # Store the content of the file as a variable
        return es.count(letter)     # Ref 1 & 2; the countEs fun now returns the count function

amountEs = countEs(filename,str("e"))  # This uses the count fun and specifies that within the filename you want 'e' counted 
print("There are {} Es in {}".format(amountEs, filename))




