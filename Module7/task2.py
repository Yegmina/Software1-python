names = set({})
#print(type(names))#for debugging

new_name=input("Enter name: ")

while new_name!="":
    previous_length=len(names)
    names.add(new_name)
    length=len(names)
    if (length==previous_length):
        print("Existing name")
    #elif(length==previous_length+1):
    #    print("New name")
    #else:
    #    print("Unexpected condition error")#for debugging

    else:
        print("New name")
    new_name = input("Enter name: ")




