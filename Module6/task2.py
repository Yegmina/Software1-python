import random

max=int(input("Enter the maximum number on the dice: "))
def roll(max):
    roll_number=random.randint(1,max)
    return roll_number

number=roll(max)
while number!=max:
    print(number)
    number=roll(max)

print(number) #max
