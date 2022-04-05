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


# import the sys module to allow command line arguments to be passed into the Python script
import sys              
# assign the filename using the CLI byget the last argument on the command line (i.e. read in the filename from the terminal, if running in VS code'; Ref 3)
filename = sys.argv[-1]

# Ref 5
def countEs(filename, letter): 
    # Open the file in read mode(text file)        
    with open(filename, 'rt') as f:  
        # Store the content of the file as a variable
        es = f.read()  
        # The countEs fun now returns the count function (Ref 1-2)             
        return es.count(letter)     

# This uses the count function and specifies that within the filename you want 'e' counted
amountEs = countEs(filename,str("e"))   
print("There are {} Es in {}".format(amountEs, filename))




