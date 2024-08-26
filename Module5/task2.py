array=[]
i=1
length=0
while i > 0:
    num = input("enter number (an empty line to quit)")
    if num =="":
        i = 0
    if num!="":
        array.append(float(num))
        length+=1

array.sort(reverse=True)
#massive=sorted(massive, reverse=True)
if length<5:
    print(array)

else:
   # while i<5:
   #     print(array[i])
   #     i+=1
    print(array[0:5])









