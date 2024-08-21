print("This is program that output perimeter and area of the rectangle. You should only provide length and width. Our program will do all calculations!")
length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))
if length>0 and width>0:
    perimeter=2*(length+width)
    area=length*width
    print("Perimeter=",perimeter)
    print("Area=",area)
else:
    print("length and width should be positive numbers")