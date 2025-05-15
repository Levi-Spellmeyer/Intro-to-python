# 1. Whats wrong with this code
# a = b = 7
# print('a = ', a, '\nb = ', b)

# When printing variables within a string there needs to an 'f' before the quotes and {} around the variables
a=b=7
print(f"a = {a} \nb = {b}")


# Funcion that uses conditionals to satisfy the Turing Test mentioned in question 3.6
def conversation():
    input("What is your problem? ")
    strYesNo=input("Have you had this problem before? (yes/no) ")
    if(strYesNo == 'yes'):
        print("Well, you have it again")
    else:
        print("Well, you have it now")
conversation()   


# Table of squares and vubes
def tableSquaresCubes():
    col1 = 'Number'
    col2 = 'Square'
    col3 = 'Cube'

    print(f"{col1:>7} {col2:>7} {col3:>6}")
    for number in range(6):
        print(f"{number:>7} {number**2:>7} {number**3:>7}")
tableSquaresCubes()


# Functiom similar to one in chpater 2. Sepearates each digit of a 5 digit number
# for Simplicity I hardcoded the five digit number
def spaceInput():
    intFiveDigitNum = 42399
    intMod=10000
    for iteration in range(5):
        if(iteration == 0):
            print(intFiveDigitNum // intMod, end = ' ')
        else:
            print(int(intFiveDigitNum % intMod // (intMod/10)), end = ' ')
            intMod //= 10
spaceInput()


# Problem given to me mentioned using a nested for loop but I figured out how to do it in one
# This is technically more time efficient
# In the book it wanted me to print each asterick with end = ''
# To complete the books question I would use 1 for loop to control the row and then 4 for loops, one for each triangle getting printed
 
def asterickTriangles():
    intTotalRows = 10
    for row in range(intTotalRows):
        print(f"{'*'*(1+row):<11} {'*'*(intTotalRows-row):<11} {'*'*(intTotalRows-row):>11} {'*'*(1+row):>11}")
asterickTriangles()


