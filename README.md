# pands-problem-sheet

## Project Descripton

My name is **Éilis Sutton** and I would like to welcome you to my first foray into programming. 

Below you will find a list of weekly tasks that I have completed ***in python*** as part of my course in the Galway-Mayo Institute of Technology (GMIT) **Higher Diploma in Computing in Data Analytics**

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

## Weekly Task 02
### Statements
#### This program calculates BMI

This week's topic explored creating simple programs using **Statements**.

* The program begins by asking the user to input their weight in kilograms (kg), following by their height in centimetres (cm). 
* It then creates a new variable that calculates BMI (weight[kg]/height[m<sup>2</sup>]), based on the user input values. 
* Finally it prints out the resulting BMI value<sup>1.

```python
# asks the user to input their weight
weight = int(input("Please enter your weight (kg):"))
# asks the user to input their height
height = int(input("Please enter your height (cm):"))
# creates a variable that calculates BMI as per the formula
newNumber = weight/((height/100)**2)
# outputs the variable based on the user input
print('The BMI is kg/m2: {}' .format (newNumber))
```
References
> 1. [Code obtained from addOne.py during Statements topic lectures](https://github.com/ESutton567/Pands2022/blob/main/Lectures/Week02/addOne.py)