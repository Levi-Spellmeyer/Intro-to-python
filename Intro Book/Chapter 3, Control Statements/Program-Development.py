""" The instructions given for this example from the book """
# Your program should analyze the results of the exam as follows:
# 1. Input each reulst (i.e a 1 or a 2). Display the message "enter result" each time the program requests another test result
# 2. Count the number of stest results of each type.
# 3. Display a summary of the test results indicating the number of students who passed and the number of students who failed
# 4. If more than eight students passed the exam, display "Bonus to instructor."


# My solution to this given scenario
def examResults(dictionary):
    intCountPass = 0
    intCountFail = 0

    for student in dictionary:
        if (dictionary[student] == 1):
            intCountPass += 1
        else:
            intCountFail += 1
    if (intCountPass >= 8):
        print("Bonus to the instructor")

    print(f"Passed: {intCountPass}")
    print(f"Failed: {intCountFail}")

# Note that a loop can be made to input any number of students and their value of 1 or 2
# You could also do a for loop that simply asks for the result of 1 or 2 after asking for the number of students who took exam
# Did not implement the continuous enter result message because I simply thought a dict would be better fit for a real world scenario
# Program could be improved by prompting for information that would go inside of dictionary instead of hard coding it
dicStudentScore = {"levi":1, "s2":2, "s3":1, "s4":1, "s5":1, "s6":1, "s7":1, "s8":1, "s9":1, "s10":2}
examResults(dicStudentScore)