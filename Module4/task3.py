numberstr=input("Enter a number: ")
if numberstr!="":
    number=float(numberstr)
    min_number=number
    max_number=number
else:
    print("not a single number has been set")
    exit()
while numberstr!="":

    number = float(numberstr)
    if number<min_number:
        min_number=number
    if number>max_number:
        max_number=number
    numberstr = input("Enter a number: ")

print("max=",max_number)
print("min=",min_number)
