number=int(input("Enter a number: "))

i=2

prime=True
if number==1: #number 1 have only one factor
    prime=False


while i<number:
    if number%i==0:
        prime=False
        break # for optimization
    i=i+1

if prime==True:
    print("The number is prime")

else:
    print("The number is not prime")
