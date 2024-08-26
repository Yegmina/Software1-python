gasoline_in_gallons=float(input("input quantity of gasoline: "))

def gallons_to_litres(gallons):
    litres=gallons*3.7854
    return litres

while gasoline_in_gallons>=0:
    print(gallons_to_litres(gasoline_in_gallons))
    gasoline_in_gallons = float(input("input quantity of gasoline"))


