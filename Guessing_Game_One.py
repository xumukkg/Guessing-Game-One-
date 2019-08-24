import random
from random import randint
print("Find random number from 1 to 20")
a = random.randint(1, 20)

while True:
    b = int(input('Guess number : '))
    if abs(b-a)==2:
        print("hot")
    elif abs(b-a)==1:
        print("too hot")
    elif abs(b-a)==0:
        print("You find a number. The number was %s " % a)
        break
    else:
        print('Cold')