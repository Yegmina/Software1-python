from random import randint

line=''
i=1
while i<=3:
    randomvar = randint(0,9)
    line=line+str(randomvar)
    i+=1


print(line)
line=''
i=1
while i<=4:
    randomvar = randint(1,6)
    line=line+str(randomvar)
    i+=1

print(line)