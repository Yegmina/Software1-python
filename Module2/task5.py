

print("This is a program that converts the input to full kilograms and grams and outputs the result to the user.")

talents = float(input("Enter talents: \n"))
pounds = float(input("Enter pounds: \n"))
lots = float(input("Enter lots: \n"))

pounds = pounds + talents * 20
lots = lots + pounds * 32
grams = lots * 13.3

kilograms = int(grams // 1000)
grams = grams % 1000

if talents>0 and pounds>0 and lots>0:
    print(f"The weight in modern units: \n{kilograms} kilograms and {grams:.2f} grams")
else:
    print("talents, pounds and lots should be positive")


