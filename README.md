# pands-problem-sheet

## Project Descripton

My name is **Éilis Sutton** and I would like to welcome you to my first foray into programming. 

Below you will find a list of weekly tasks that I have completed ***in python*** as part of my course in the Galway-Mayo Institute of Technology (GMIT) **Higher Diploma in Computing in Data Analytics**

---
Suggested tools to run these programs:
* [Visual Studio Code (VSC)](https://code.visualstudio.com/) 
* [Python 3.8 or higher](https://www.python.org/)
---
Within this ReadMe I will cover programs that:
- Calculate BMI *(week 2)*
- Ask a user to input a string and outputs every second letter in reverse order *(week 3)*
- Run the collatz conjecture *(week 4*)
- Output whether or not today is a weekday *(week 5*)
- Takes a positive floating-point number as input and outputs an approximation of its square root without using built in functions *(week 6*)
- Read in a text file and outputs the number of e's it contains *(week 7*)
- Display a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes *(week 8*)

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
# ask the user to input their weight
weight = int(input("Please enter your weight (kg):"))
# ask the user to input their height
height = int(input("Please enter your height (cm):"))
# create a variable that calculates BMI as per the formula
newNumber = weight/((height/100)**2)
# output the variable based on the user input
print('The BMI is kg/m2: {}' .format (newNumber))
~~~
References
> 1. [Code obtained from addOne.py during Statements topic lectures](https://github.com/ESutton567/Pands2022/blob/main/Lectures/Week02/addOne.py)

---

## 3. Variables

    This week explored the topic of variables.

    The weekly task was to write a program that takes string inputted by the user and outputs every second letter in reverse order 

#### **secondtring.py**

* This program begins by asking the user to input a sentance (argument). 
* It then slices the inputted argument to every other character of the input argument from index 0 (0 being the first character) to the end ([::2]<sup>1) 
* To retrieve these characters in reverse order add a minus in to [::2] -> [::-2]<sup>2 
* Finally it prints out the resulting message.

~~~python
# ask the user to enter a sentance
# slice the argument to every 2nd element, and reverse it
message = input("Please enter a sentance: ")[::-2] 
# print the message
print(message)
~~~
References
> 1. [stackoverflow.com](https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python)
> 2. [realpython.com](https://realpython.com/reverse-string-python/)

---