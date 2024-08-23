gender=input("Enter your gender")
hemoglobin=int(input("Enter your hemoglobin")) #it doesn't say, but we'll assume hemoglobin is an integer.
if gender=="Male" or gender=="male" or gender=="M" or gender=="m":
    if hemoglobin<117:
        print("hemoglobin is low")
    elif hemoglobin<=155:
        print("hemoglobin is normal")
    else:
        print("hemoglobin is high")

elif gender=="Female" or gender=="female" or gender=="F" or gender=="f":
    if hemoglobin<134:
        print("hemoglobin is low")
    elif hemoglobin<=167:
        print("hemoglobin is normal")
    else:
        print("hemoglobin is high")