# Converts the number input taken in as a string to int and stores the value in rating
rating = int(input("Enter an integer rating between 1 and 10: "))


# Simple if statement and comaparrison operator
grade = int(input("Enter grade: "))
if grade >= 90:
    print("Congradulations your grade of", grade, "earns you an A!")

# Function to check if a number is odd or even
def oddOrEven(num):
    if (num % 2 != 0):
        print(num, "is odd")
oddOrEven(5)


# Function prompts user to enter a 5 digit number and then splits each digit of that number apart with 3 spaces in bettween
def spaceInput():
    strInput = int(input("\nEnter a 5 digit number here: "))

    if(strInput <= 9999):
        while(strInput <= 9999):
            print("Invalid number. I guess you do not know how to read.")
            strInput = int(input("Enter a 5 digit number here: "))

    firstDigit = strInput // 10000
    secDigit = strInput % 10000 // 1000
    thirdDigit = strInput % 1000 // 100
    fourthDigit = strInput % 100 // 10
    fithDigit = strInput % 10 // 1

    print(firstDigit,"   ", secDigit,"   ", thirdDigit,"   ", fourthDigit,"   ", fithDigit)
spaceInput()