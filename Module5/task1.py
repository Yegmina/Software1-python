from random import randint

dice_to_roll=int(input("How many dice to roll? "))
sum=0

if dice_to_roll<0:
    print("You must enter a positive integer number")
    exit()
for i in range(1,dice_to_roll+1):
    #print(i)
    number=randint(1,6)
    print(f"dice {i}: number {number}")
    sum=sum+number

print(f"The sum is {sum}")