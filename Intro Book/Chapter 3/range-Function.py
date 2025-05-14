# Note all number will be printed on same line as end=' ' adds a space to each output
# tells python to replace the default newline with an empty space
for number in range(99, -1, -11):
    print(number, end=' ')


# Note each number in this loop will get its own line
# Default value at the end of each print statement is a newline
for number in range(99, -1, -11):
    print(f"{number} ")


# Use range function to sum even int from 2 through 100
intTotal = 0
for number in range(2,101,2):
    intTotal += number
print(intTotal)