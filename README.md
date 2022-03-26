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

#### **secondstring.py**

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

## 3. Controlling the flow

This week explored flow control: assigning conditions to statements and implementing iterations using 'for' loops and 'while' loops.

The weekly task was to run the Collatz Conjecture on a user input value.

The [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture):
>"...in mathematics asks whether repeating two simple arithmetic operations will eventually transform every positive integer into one. It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1."

#### **collatz.py**

* This program begins by creating a function to run the Collatz Conjecture<sup>1</sup>. A conditional statement is applied that if the argument (number) is even then it is to be divided by 2. If the number is not even, i.e. it is odd, then the number will be multipled by 3 and a 1 subsequently added. 
* The program will print the output
* The user is asked to enter an integer
* The program will enter this value into the Collatz function repeatedly until the function outputs a value of 1. 
* When this last step occurs the program will be terminated<sup>2</sup>

~~~python
This program asks the user to input any positive integer and outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Author: Éilis Sutton
# Ref 1: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# Ref 2: https://java2blog.com/exit-program-python/

def collatz(number):                  # Ref 1 - create function for collatz conjecture
    if number % 2 == 0:               # if the argument is even
        print(number // 2)            # print argument value divided by 2
        return number // 2            # call function to divide argument value by 2
    
    elif number % 2 == 1:             # If the number is odd
            result = ((3*number) +1)  # print the argument multipled by 3 first then add 1 to this
            print(result)             # print input argument divided by 2
            return result             # call function to multiple input argument by 3, then add one
           
numberInput = int(input("Please enter a positive integer: "))
while numberInput != 1:               # keep rerunning the function until the argument passed into the function equals 0
    numberInput = collatz(numberInput)# pass the argument value into the collatz function
else: 
    numberInput == 1
    quit()                            # ref 2 - quit the program when a specific output value returns back into the function
~~~
References
> 1. [stackoverflow.com](https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff)
> 2. [java2blog.com](https://java2blog.com/exit-program-python/)

---