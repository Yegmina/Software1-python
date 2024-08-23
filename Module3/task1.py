length=int(input("Enter the length of a zander in centimeters"))

min_length=42

if length<min_length:
    print("Release the fish back into the lake!")
    print("zander should be at least", min_length-length, "longer")