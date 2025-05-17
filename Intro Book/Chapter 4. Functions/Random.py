import random

for roll in range(10):
    print(random.randrange(1,7), end=' ')
    # randrange generates an integer from the firts argument value up to but not including the second



def flipCoin(intNumFlips):
    for i in range(intNumFlips):
        print('H' if random.randrange(2) == 0 else 'T', end=' ')
flipCoin(10)