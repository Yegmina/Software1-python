import random

def roll():
    roll_number=random.randint(1,6)
    return roll_number

number=roll()
while number!=6:
    print(number)
    number=roll()

print(number) #6
