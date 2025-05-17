# Chapter 4: Functions

## 4.1) Introduction
- divide and conquer: The idea that the best way to develop and maintain a large program is  to construct it from smaller more manageable pieces
- Creating functions allows code to be reused more easily and makes programs easier to modify

<br>

## 4.2) Defining Functions
- A function definition begins with the `def` keyword followed by the the function name and a set of parentheses and a colon `():`
- inside the parentheses is where you will define the funtion's parameter list (comma seperated list)
- This list contians the values needed for the function to perform its task
- If a function returns none, it is implicitly returns the value none/false
- The function body is referred to as its block

<br>

## 4.3) Functions with Multiple Parameters
- A function with multiple parameters specifies them as a comma seperated list
- Nothing new to take note of

<br>

## 4.4 Random Number Generation
* Note Examples in random.py
- When using the randrange function: using `random.seed({some int})` will ensure the 'random' sequence is the same
- This allows you to test logic while using the same numbers

<br>

## 4.5) Case Study: A Game of Chance
- Tuple: unmodifiable sequence of values. To create a tuple, separate its values with commas
ex.) tuple1 = (var1, var2)
- Note the parentheses are optional but recommended for clarity
- To use a tuples values, you can assign them to a comma separated list of variables (unpacking the tuple)
ex.) num1, num2 = tuple1
- `in` operator whethers the value on the left is present in the value on the left:
ex.) if 7 in (7, 11): this executes as true and underlying statements would be ran
- Note: There is also a `not in` operator

<br>

## 4.6) Python Standard Library
1. datetime: date and time manipulations. Also modules time and calendar
2. os: used for interacting with the operating system
3. sys: Command-line arguement processing
4. webbeowser: display web pages in Python apps

<br>

## 4.7) math Module Functions
- To use a modules definition, use the modules name and a dot: module.function()
- Specific math functions listed on pg. 133

<br>

## 4.8) Using IPython tab completion for Discovery
- Nothing worth taking note of

<br>

## 4.9) Default Parameter Values
- when calling a function you can omit the argument for a parameter with a default value which is automatically passed
* ex.) `def rectangle_area(length=2, width=3)`
- Simply include an `=` and the desired value for a parameter sets its default value
- Parameters with default values must be listed to the right of those without
- In the above example if we called the function like `rectangle_area(10)` it would set length=10 as parameters are assigned from left to right 

<br>

## 4.10) Keyword Arguments
- Nothing to take note of

<br>

## 4.11) Arbitrary Arguments Lists
- Built in functions like max and min can receive any number of arguments
- To define a function with an arbitrary argument list:
    * `def average(*args):`
- you can unpack a tuple, list or other iterable element to pass them as individual function arguments using the `*` operator
    * `grades=[1,2,3,4]`        `function_name(*grades)`

<br>

## 4.12) Methods: Functions that belong to Objects
- A method is afunction the you call on an object using the form `object_name.method_name(arguments)`

<br>

## 4.13) Scope Rules
- Local Scope: Typically shown in variables defined in functions that can only be used inside the function (local)
- Global Scope: Variables that are identified outside any function or class, can access anywhere or in any function
- Note you cannot modify a global variable in a function
- To modify a global variable you must use the `global` statement

<br>

## 4.14) import: A Deeper Look
- To import multiple identifiers: `from module import 1, 2`
- Binding names for modules and module identifiers: `import module as {chosen name}`

<br>

## 4.15) Passing Arguments to Functions: A deeper Look
1. Pass-by-value: the function receives a coy of the arguments value. Changes to this value do not affect the origional value.
2. Pass-by-reference: The function can access the arguments value in the caller directly and modify the value if mutable.
- Python argument are always passed by reference


## 4.16) Function call stack
- Last in first out data structure


## 4.17) Functional-style Programming
- Using functions keeps your programs simplier and easier to read/debug



## 4.19) Wrap-up