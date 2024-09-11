import mariadb
from geopy.distance import geodesic



def get_airport_coordinates(icao_code):

    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao_code}';"


    cursor = connection.cursor()


    cursor.execute(sql)


    result = cursor.fetchone()


    if result:
        latitude, longitude = result
        return latitude, longitude
    else:
        print(f"No coordinates found for ICAO code: {icao_code}")
        return None


try:
    connection = mariadb.connect(
        host='127.0.0.1',
        port=3306,
        database='test',
        user='root',
        password='3560',
        autocommit=True
    )

    icao_code_1 = input("Enter the ICAO code of the first airport: ")
    icao_code_2 = input("Enter the ICAO code of the second airport: ")

    coordinates_1 = get_airport_coordinates(icao_code_1)
    coordinates_2 = get_airport_coordinates(icao_code_2)

    #print(type(coordinates_2))

    if coordinates_1 and coordinates_2:
        distance = geodesic(coordinates_1, coordinates_2).kilometers
        print(f"The distance between {icao_code_1} and {icao_code_2} is {distance:.2f} kilometers.")
    else:
        print("Could not calculate distance because one or both ICAO codes were invalid.")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

finally:
    if connection:
        connection.close()
