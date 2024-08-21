import cmath

print("This is program that output area of the circle. You should only provide radius and our program will do calculations!")
radius = float(input("What is the radius?"))
area= float(cmath.pi * radius ** 2)
areastring=str(area)
print("Area="+areastring)