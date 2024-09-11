import mariadb


def get_airport_info(local_input_ICAO):
    sql = f"select name, municipality from airport where ident='{local_input_ICAO}';"

    cursor = connection.cursor()

    cursor.execute(sql)

    result = cursor.fetchall()

    if cursor.rowcount > 0:
        name, municipality = result[0]
        #    print(f"Airport name : {name}, location: {municipality}")
        return name, municipality
    else:
        print("No records found.")
        return None, None



try:
    connection = mariadb.connect(
        host='127.0.0.1',
        port=3306,
        database='test',
        user='root',
        password='3560',
        autocommit=True
    )

    global_input_ICAO = input("Input ICAO of the airport: ")

    name, municipality = get_airport_info(global_input_ICAO)

    if name and municipality:
        print(f"Airport name : {name}, location: {municipality}")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

finally:
    if connection:
        connection.close()
