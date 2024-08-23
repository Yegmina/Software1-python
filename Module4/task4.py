import random

random_number=random.randint(1,10)

quess=int(input("try to guess the number from 1 to 10: "))

while quess!=random_number:
    if quess<random_number:
        print("Too low")
    elif quess>random_number:
        print("Too high")
    quess = int(input("try to guess the number from 1 to 10: "))

print("Correct")