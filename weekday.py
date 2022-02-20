# This program outputs whether or not today is a weekday
# Éilis Sutton
# Ref 1: https://www.w3schools.com/python/python_datetime.asp
# Ref 2: https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python

import datetime             # This imports the 'datetime' module

weekNumber = datetime.datetime.today().weekday()  # Gets the weekday number (1-7)

if weekNumber < 5:
    print("Yes, unfortunately today is a weekday.")
else: 
    print("It is the weekend")
