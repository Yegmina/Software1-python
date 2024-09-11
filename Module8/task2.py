import mariadb
'''
Write a program that asks the user to enter the area code (for example FI) 
and prints out the airports located in that country ordered by airport type. 
For example, Finland has 65 small airports, 15 helicopter airports and so on.
'''


def print_airport_from_area(local_input_code):
    sql = f"select name, type from airport where iso_country='FI' order by type desc;"

    cursor = connection.cursor()

    cursor.execute(sql)

    result = cursor.fetchall()

    for row in result:
        print(row)



try:
    connection = mariadb.connect(
        host='127.0.0.1',
        port=3306,
        database='test',
        user='root',
        password='3560',
        autocommit=True
    )


    #global_input_code = input("Input area code of the airports: ")
    global_input_code="FI"
    print_airport_from_area(global_input_code)




except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

finally:
    if connection:
        connection.close()
