import random

total=int(input("Enter a number (how many random points to generate): "))
N=total
i=1
n=1
while i<=total:
    x=random.uniform(-1, 1)
    y=random.uniform(-1, 1)
    if x**2+y**2<1:
        n=n+1
    i=i+1

pi=4*n/N
print("pi=", pi)

'''
test
Enter a number (how many random points to generate): 100000000
pi= 3.14166968
'''

