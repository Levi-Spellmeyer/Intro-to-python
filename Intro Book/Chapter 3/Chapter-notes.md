# Chapter 3: Control Statements and Program Development

## 3.1) Introduction
- Nothing to take note of

<br>

## 3.2) Algorithms
- Program control specifies the order in which statements execute in a program

<br>

## 3.3) Pseudocode
- The process of thinking out algorithms in an english code mix

<br>

## 3.4) Control Statements
- Statements usually execute in the order they are written
- `if ... else` if condition if True or perform differrent action if condition False
- `if...elif...else` performs one of many different actions depending on truth of several conditions

<br>

## 3.5) if Statement
- Nothing important to take note of

<br>

## 3.6) if..else and if...elif...else statements
- Important to take note of syntax `elif` not `else if`
- Ending an elif chain with else is optional
- `else` cannot come before and `elif`

<br>

## 3.7) while Statement
- Nothing new here to take note of

<br>

## 3.8) for Statement
- `print(10, 20, 30, sep=', ')` will print the numbers listed with a comma and space between them
- `range()` function creates an iteratble object that rerpresents a sequence of integer values starting from 0 and continuing up to but not including the argument value. range(10) = 0-9

<br>

## 3.9) Augmented Assignments
- Abbreviation of assignment expressions in which the same variable name appears on left and right side of '='
1. +=       c += 7      c = c + 7
2. -=
3. *=
4. **=
5. /=
6. //=
7. %=

<br>

## 3.10) Program Development: Sequence-Controlled Repetition
- requirement statement describes what a program is supposed to do but not how the program should do it
- initialization phase: creates varaibles and set them to the proper initial values
- processing phase: process the data and do required calculations
- termination phase: displays output and cleans up final processes
- and f string look like: `f'some text {variable}'`, this allows variables to be put in quotes

<br>

## 3.11) Program Development: Sentinel-Controlled Repetition
- signal value, dummy value, and flag value are substitute name for a sentinel value (used to indicate end of data entry)

<br>

## 3.12) Nested control statements
- Completed example in ProgramDevelopment.py
- Otherwise no notable concepts

<br>

## 3.13) Built-in function range
- `for number in range(5, 10)` produces a sequence of integers from its first argument up to but not including the second argument value
- `range(0, 10, 2)` produces sequence of int from its first arguement up to but not including the second argument incrementing by its third
- Can also decrement: `range(10, 0, 1)`
- Example work in range-function.py

<br>

## 3.14) Using Type Decimal for Monetary Amounts
- `printf'{variable:.20f}'` the .20f specifies that you want the output to print 20 digits to the right of the decimal
- Examples using the Decimal standard library are in Decimal.py
- Decimals support the sstandard arithmetic operators of +,=,/,//,*,%, an **
- You can perform arithemetic between Decimals and ntegers but not between Decimals and floating point numbers (121.34)

<br>

## 3.15) Breaks and continue statements
- `break` and `continue` can alter a loop's flow
- break: when used in a while or for loop, immediately exits the statement/loop
- continue: when used in a while or for loop skips the remainder of the loop. Ex) in a for loop, if valuee == 5 continue, skips iteration where value  == 5

- to left align: `{variable:<10}` 
- Note commonly need to use f stringgs to use the :<# alignment attribute

<br>

## 3.16) Boolean operators (and, or, not)
- Nothing new here. Just note that and, or, not are commonly used in conditional statements with multiple conditions var1 == 2 or var1 == 3
- Note that the keyword `not` reverses the meaning of a condition

<br>

## 3.17) Intro to Data Science: Mean, Median, and Mode
- Mean is the average value in a set of vales
- Median is the middle value when all values are arranged in sorted order
- Mode is the most frequently occuring value
- `sum(list of nums)` returns the sum of a list of int
- `len(list)` returns the len of a specified list
- Note the statistics module provides function for calculatingthe mean median and mode (a few side notes in statistics.py)
