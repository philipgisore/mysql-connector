import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user = "philip",
        password = "Worldw@rz700#",
        database = "Student"
    )
    if connection.is_connected():
        print("Successfully connected to MySQL database!")

except Error as e:
    print(f"Error while connecting to MySQl: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")