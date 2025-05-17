def squareRoot(number):
    intSqrt = number ** (1/2)
    return intSqrt
# alternatively you could remove the local variable and simply `return number ** 1/2``

number = float(input("Enter the number you wish to know the square root of: "))
print(squareRoot(number))