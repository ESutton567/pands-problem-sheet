# pands-problem-sheet

## Project Descripton

My name is **Éilis Sutton** and I would like to welcome you to my first foray into programming. 

Below you will find a list of weekly tasks that I have completed in **Python** as part of my course in the [Atlantic Technological University (ATU)](https://www.gmit.ie/) (previously the Galway-Mayo Institute of Technology [GMIT]) **Higher Diploma in Computing in Data Analytics**

---
Suggested tools to run these programs:
* [Visual Studio Code (VSC)](https://code.visualstudio.com/) 
* [Python 3.8 or higher](https://www.python.org/)
---

The below table lists the topics that were covered each week, the programs assigned as part of the weekly tasks and links to the code on [Github](https://github.com/).

| Weekly Task Number | Topic | URL|
|:-----------:|:-------------|:-------------|
| 1  | Creating a repository|[pands-problem-sheet](https://github.com/ESutton567/pands-problem-sheet)|
| 2  | Statements   |[bmi.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/bmi.py)|
| 3  | Variables    |[secondstring.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/secondstring.py)|
| 4  | Controlling the flow |[collatz.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/collatz.py)|
| 5  | Data         |[weekday.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/weekday.py)|
| 6  | Functions    |[squareroot.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/squareroot.py)|
| 7  | Files        |[es.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/es.py)|
| 8  | Plotting |[plottask.py](https://github.com/ESutton567/pands-problem-sheet/blob/main/plottask.py)     |

---

## 2. Statements

This week's topic explored creating simple programs using statements.

The weekly task was to write a program to calculate a user's Body Mass Index (BMI)

#### **BMI.py**

* This program begins by asking the user to input their weight in kilograms (kg), following by their height in centimetres (cm). 
* It then creates a new variable that calculates BMI (weight[kg]/height[m<sup>2</sup>]), based on the user input values. 
* Finally it prints out the resulting BMI value<sup>1.

~~~python
# Ref 1 - ask the user to input their weight
weight = int(input("Please enter your weight (kg):"))
# ask the user to input their height
height = int(input("Please enter your height (cm):"))
# create a variable that calculates BMI as per the formula
newNumber = weight/((height/100)**2)
# output the variable based on the user input
print('The BMI is kg/m2: {}' .format (newNumber))
~~~

* To run this program enter the following into the command line:
~~~ 
python bmi.py 
~~~

References
> 1. [Code obtained from addOne.py during Statements topic lectures](https://github.com/ESutton567/Pands2022/blob/main/Lectures/Week02/addOne.py)

---

## 3. Variables

This week explored the topic of variables.

The weekly task was to write a program that takes a string inputted by the user and outputs every second letter in reverse order.

#### **secondstring.py**

* This program begins by asking the user to input a sentance (argument). 
* It then slices the inputted argument to every other character of the input argument from index 0 (0 being the first character) to the end ([::2]<sup>1). 
* To retrieve these characters in reverse order add a minus in to [::2] -> [::-2]<sup>2.
* Finally it prints out the resulting message.

~~~python
# ask the user to enter a sentance
# slice the argument to every 2nd element, and reverse it
message = input("Please enter a sentance: ")[::-2] 
# print the message
print(message)
~~~

* To run this program enter the following into the command line:
~~~ 
python secondstring.py 
~~~

References
> 1. [stackoverflow.com](https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python)
> 2. [realpython.com](https://realpython.com/reverse-string-python/)

---

## 4. Controlling the flow

This week explored flow control: assigning conditions to statements and implementing iterations using 'for' loops and 'while' loops.

The weekly task was to run the Collatz Conjecture on a user input value.

The [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture):
>"...in mathematics asks whether repeating two simple arithmetic operations will eventually transform every positive integer into one. It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1."

#### **collatz.py**

* This program begins by creating a function to run the Collatz Conjecture<sup>1. A conditional statement is applied that if the argument (number) is even then it is to be divided by 2. If the number is not even, i.e. it is odd, then the number will be multipled by 3 and a 1 subsequently added. 
* The user is asked to enter an integer which is run through the collatzz function
* The output of this is then printed and reentered back into the function to run repeatedly until the the function outputs a value of 1 (using a while loop). 
* When the function returns an output of 1, the program will be terminated<sup>2.

~~~python
# Ref 1 - create function for collatz conjecture
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
    # Ref 2 - quit the program when a specific output value returns back into the function
    quit()  
~~~

* To run this program enter the following into the command line:
~~~ 
python collatz.py 
~~~

References
> 1. [stackoverflow.com](https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff)
> 2. [java2blog.com](https://java2blog.com/exit-program-python/)

---

## 5. Data

This week explored data structures including:
- lists
- tuples
- dictionaries

The weekly task was to create a program that outputs whether the current day is a weekday or not.

#### **weekday.py**

* This program uses an in-built module of Python called datetime, which supplies classes for manipulating dates and times<sup>1. 
* It then sets a variable to be equal to the weekday number where 0-6 equate to the 7 days of the week (Monday-Sunday, with Monday beginning at 0).
* It subsequently gives two printing options when run, depending on the day of the week that the program is run. That it is a weekday if run on Monday to Friday (weekday numbers 0-4) or a weekend if run on Saturday or Sunday (weekday numbers 5 and 6)<sup>2.

~~~python

# Ref 1-2 - import the 'datetime' module
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
~~~

* To run this program enter the following into the command line:
~~~ 
python weekday.py 
~~~

References
> 1. [w3schools.com](https://www.w3schools.com/python/python_datetime.asp)
> 2. [tutorialsrack.com](https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python)

---

## 6. Functions

This week explored functions.

The weekly task was to create a program that takes a floating point number as the input and outputs an approximation of it's square root, without using the in-built functions x**.5 or math.sqrt(x).

#### **squareroot.py**

* This program creates a function to calculate the square root of a number that the user inputs.
* The algorithm employed to find the root of the number is Newton's Method<sup>1,2</sup>.

[Newton's Method](https://en.wikipedia.org/wiki/Newton%27s_method):
> "...a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function."

* Firstly, the program asks the user to input a positive number.
* It then enters the number into the function, runs it through an equation (x = x - (x multiplied by x minus y) divided by (2 multiplied by x), and it does this 6 times to improve on the accuracy of the root output number. 
* It then outputs a sentence that lets the user know what the root value is of the number they chose.

~~~python

# ask the user to input a positive float number
num1 = float(input("Please enter a positive number: "))

# Ref: 1-2 - Use Newton's method to write a square root algorithm 
# create a function called sqrt 
def sqrt(y: float) -> float:
    x: float = y
    # Ref 2 - set a range to run Newton's method equation that follows below 6 times 
    # (6 repeats seems to return a fairly accurate redult. No need to go higher)
    for _ in range (0,6):  
        # Asking: x^2 - y = 0 (y [slope] is a known constant)        
        x = x - (x * x - y) / (2 * x)   
    # call the function
    return x            

# create a new variable equal to the function with the user argument (user inputted float number) inserted into the function
# make sure to include the whole function name here
ans = sqrt(num1) 
# print the new variable, which is the output of the function         
print ("The square root of 14.5 is approx {} ".format (ans)) 

~~~

* To run this program enter the following into the command line:
~~~ 
python squareroot.py 
~~~

References
> 1. [stackoverflow.com](https://stackoverflow.com/questions/1623375/writing-your-own-square-root-function)
> 2. [youtube.com](https://www.youtube.com/watch?v=3i9KozCUKU4)

---

## 7. Files

This week's topic covered reading and writing to files, including an introduction to JavaScript Object Notation (JSON).

The weekly task was to write a program that reads in a text file from the command line and outputs the number of e's it contains.

The text file [moby-dick.txt](https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt) was downloaded from the Github website for this purpose<sup>4</sup>.


#### **es.py**

* Firstly, the ```sys``` module is imported and instructions follow to read in the filename from the terminal (if running in VS code)<sup>3</sup>.
    * The ```sys.argv[x]``` command takes an argument from the command line and inserts it into the python code<sup>3</sup>.
    * For the purpose of this program, it allows the user to enter a filename in the command line interface (VSC terminal), after instructing the program to run. In this case, x = 1 will insert the argument that follows the ```python es.py``` instruction to run the program.
    * If the user were to enter x  = 0, this would insert the name of the running program<sup>3</sup>.
    * This will get the last argument on the command line. If no arguments are passed, it will be the script name itself, as sys.argv[0] is the name of the running program.
    * Where sys.argv[0] is the name of the running program (as no arguments are passed), sys.argv[1] gets the last argument on the command line<sup>3</sup>.

* A function is then used to count and return the number of e's that occur in the txt file<sup>5</sup>. Firstly the file is opened in read mode. The contents of the file are stored as a variable and then instructions are given to return the function as a count function<sup>1,2</sup>.

* Lastly, the count function is instructed to count the e's in the txt file and prints it out. 

~~~python

# import the sys module to allow command line arguments to be passed into the Python script
import sys              
# assign the filename using the CLI byget the last argument on the command line (i.e. read in the filename from the terminal, if running in VS code'; Ref 3)
filename = sys.argv[-1]

def countEs(filename, letter):        # Ref 5 
    with open(filename, 'rt') as f:  # Open the file in read mode(text file)
        es = f.read()               # Store the content of the file as a variable
        return es.count(letter)     # The countEs fun now returns the count function (Ref 1-2)

amountEs = countEs(filename,str("e"))  # This uses the count function and specifies that within the filename you want 'e' counted 
print("There are {} Es in {}".format(amountEs, filename))
~~~

* To run this program enter the following into the command line (while ensuring the moby-dick.text file is within the working directory):
```es.py moby-dick.txt```

References
> 1. [pythonexamples.org](https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/)
> 2. [www.w3schools.com](https://www.w3schools.com/python/ref_list_count.asp)
> 3. [stackoverflow.com](https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input)
> 4. [gist.githubusercontent.com](https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt)
> 5. [www.geeksforgeeks.org](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/)

---

## 7. Plotting

This week's topic covered plotting, with the [**matplotlib**](https://matplotlib.org/) module.

The weekly task was to write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#### **plottask.py**

* Firstly, the [**NumPy**](https://numpy.org/) module is imported to allow the program to work with array data. 
* Secondly, matplotlib is imported to allow plotting functions within the program.
* Subsequent modules are imported to enable customisation of the plot.

* A range [0,4] is assigned to a variable x.
* 3 functions are created to define the required functions :f(x)=x, g(x)=x2 and h(x)=x3<sup>3</sup>.
    * As we are working with array data we can use simple algebra to achieve this. 

* The commented out code that follows is used to test that these functions are running correctly. 

* Each function is then plotted separately<sup>4</sup>, and the plot line styles<sup>5</sup>, colours <sup>8</sup> and labels<sup>1</sup> are customised.

* A legend and axis labels are added, followed by a title with a customised font<sup7,9</sup> and finally a footnote<sup>11</sup>.

 ~~~python

# Ref 1- import package to work with array data
import numpy as np                  
# Ref 1 - pyplot is a state-based interface to matplotlib
import matplotlib.pyplot as plt     
from matplotlib import rc
# import BOLD font
from tkinter.font import BOLD
# import font properties from matplotlib font manager
from matplotlib.font_manager import FontProperties

# assign the range to the variable x (as an array)
x = np.array([1,4])             

# Ref 3 - define f(x)
def f(x):                       
    return x

def g(x):
    # we can simply multiply (to power x to 2) in this way as x an array
    return x * x                

def h(x):
    # power x to 3
    return x ** 3               

# use the code below to test that the functions work
# print(f(x), g(x), h(x))       

# Ref 4 - plot each function separately and assign colour
# Ref 5 - line style
# Ref 8 - list of colors in matplotlib
# Ref 10 - using subscript text
plt.plot(x, f(x), color='navy', label='f(x) = x')  
plt.plot(x, g(x), color='royalblue', label=r'g(x) = $x^2$', ls='--') 
plt.plot(x, h(x), color='deepskyblue', label=r'y(x) = $x^3$', ls=':')     

# Ref 1 - legends and labels
plt.legend()
plt.xlabel('x',fontweight=BOLD)
plt.ylabel('y',fontweight=BOLD)

# Ref 7 - titling and formating font 
# Ref 9 - fontweight 
plt.title(
    label='Maths Functions',
    fontname='Times New Roman',
    fontsize=14, 
    fontweight=BOLD
    )

# Ref 11 - customise text
plt.text(
    2.5, 
    -11, 
    "Produced by Éilis Sutton", 
    fontname="Times New Roman", 
    fontsize=9, 
    color='black', 
    ha='center',
)

# Ref 1 - call a visual of the the plot
plt.show()                      
~~~

* To run this program enter the following into the command line:
~~~ 
python plottask.py 
~~~

* A visual of the plot is then called which can be accessed here: [Maths Functions](plot.png)


References
> 1. [lab8.10](https://github.com/ESutton567/Pands2022/blob/main/Labs/Week08-plotting/lab8.10-counties.py)
> 2. [www.w3schools.com](https://www.w3schools.com/python/matplotlib_plotting.asp)
> 3. [calc-again.readthedocs.io](https://calc-again.readthedocs.io/en/latest/tutorials/01-plotting-and-functions.html)
> 4. [scriptverse.academy](https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html)
> 5. [www.w3schools.com](https://www.w3schools.com/python/matplotlib_line.asp)
 >6. [www.w3schools.com](https://www.w3schools.com/python/matplotlib_labels.asp)
> 7. [www.geeksforgeeks](https://www.geeksforgeeks.org/matplotlib-pyplot-title-in-python/)
> 8. [matplotlib.org](https://matplotlib.org/stable/gallery/color/named_colors.html)
> 9. [stackoverflow.com](https://stackoverflow.com/questions/18962063/matplotlib-setting-title-bold-while-using-times-new-roman)
> 10. [www.tutorialspoint](https://www.tutorialspoint.com/how-to-write-text-in-subscript-in-the-axis-labels-and-the-legend-using-matplotlib)
> 10. [python-graph-gallery.com](https://python-graph-gallery.com/web-line-chart-with-labels-at-line-end)

---