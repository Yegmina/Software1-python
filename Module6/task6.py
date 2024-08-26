

def pizza_unit_price(diameter,price):
    area=3.14*(diameter/2)**2
    unit_price=area/price
    return unit_price/10000 #converting to square meter

diameter1=float(input("Enter the diameter of the first pizza:"))
price1=float(input("Enter the price of the first pizza:"))

diameter2=float(input("Enter the diameter of the second pizza:"))
price2=float(input("Enter the price of the second pizza:"))

if pizza_unit_price(diameter1,price1)<pizza_unit_price(diameter2,price2):
    print("second pizza is more expensive than first pizza")

elif pizza_unit_price(diameter1,price1)>pizza_unit_price(diameter2,price2):
    print("second pizza is less expensive than first pizza")

else:
    print("prices per unit are equal")



