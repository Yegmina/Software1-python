print("write 'info' for fetching information of an existing airport\n 'new' for  entering a new airport\n 'quit' to stop the script")
ICAO = {"EFHK":"Helsinki-Vantaa Airport"}


choice=input("Enter your choice: ")

def info():
    icao_info=input("enter the ICAO code: ")
    print(ICAO[icao_info])
    return 0

def new():
    icao_new=input("enter the ICAO code: ")
    name_new=input("enter the name of the airport: ")
    ICAO[icao_new]=name_new
    return 0

while choice!="quit":

    if choice=="info":
        info()
    elif choice=="new":
        new()
    else:
        print("you can use only quit, info, new commands")

    #print(choice)
    choice = input("Enter your choice: ")

print("quit command entered, script stopped")