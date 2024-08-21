from random import random
from random import randint

line=''
randomvar = int(random()*1000)
line=line+str(randomvar)


print(line)
line=''
i=1
while i<=4:
    randomvar = randint(0,6)
    line=line+str(randomvar)
    i+=1

print(line)