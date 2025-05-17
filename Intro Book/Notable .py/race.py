import random
import time

# This function calculates and updates the tortois's location in the race
def tortoise(intCurrentSquare):
    intRandomMove = random.randrange(1,11)

    if (1 <= intRandomMove and intRandomMove <= 5):
        return intCurrentSquare + 3
    elif (6 <= intRandomMove and intRandomMove <= 7):
        return intCurrentSquare - 6
    elif (8 <= intRandomMove and intRandomMove <= 10):
        return intCurrentSquare + 1

# Same funcionality as tortoise function but for the hare
def hare(intCurrentSquare):
    intRandomMove = random.randrange(1,11)

    if (1 == intRandomMove or intRandomMove == 2):
        return intCurrentSquare
    elif (3 == intRandomMove or intRandomMove == 4):
        return intCurrentSquare + 9
    elif (intRandomMove == 5):
        return intCurrentSquare - 12
    elif (intRandomMove >= 6 and intRandomMove <= 8):
        return intCurrentSquare + 1
    elif(intRandomMove >= 9):
        return intCurrentSquare - 2




def main():
    input("The race will start on your call! ")
    print("BANG ! ! ! ! !")
    print("And they're off!!")


    intTortoiseLocation = 1
    intHareLocation = 1
    boolWinner  = False

# While loop that runs the race until the T or H crosses the finish line (has a location >= 70)
    while(boolWinner == False):
        intTortoiseLocation = tortoise(intTortoiseLocation)
        intHareLocation = hare(intHareLocation)


        if (intHareLocation < 1):
            intHareLocation = 1
        if(intTortoiseLocation < 1):
            intTortoiseLocation = 1
        
        # Debug statement to check location int values
        print(intTortoiseLocation, " ", intHareLocation)

        print(" ")
        for char in range(70):
            if (intTortoiseLocation == char):
                print("T", end=" ")
            elif (intHareLocation == char):
                print("H", end=" ")
            else:
                print("-", end=" ")

        if (intTortoiseLocation >= 70):
            print("\nTORTOISE WINS!!! YAY!!!")
            boolWinner = True
        elif (intHareLocation >= 70):
            print("\nHare wins. Yuck")
            boolWinner = True
        
        #Added a sleep timer so the programs progression could be followed more easily
        time.sleep(.5)
    return 0
main()