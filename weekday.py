# This program outputs whether or not today is a weekday
# Éilis Sutton
# Ref 1: https://www.w3schools.com/python/python_datetime.asp
# Ref 2: https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python

# import the 'datetime' module (Ref 1 and 2)
import datetime              
# instruct to get the weekday number (1-7)
weekNumber = datetime.datetime.today().weekday()    

# set the condition to print that it is a weekday 
# if the weeknumber is between 0-4 (i.e Mon-Fri)
if weekNumber < 5:                                  
    print("Yes, unfortunately today is a weekday.")
# if it is not between 0-4, print that it is a weekend
else: 
    print("It is the weekend")
