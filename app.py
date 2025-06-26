import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

#load variable from .env
load_dotenv()
print("Host:", os.getenv("DB_HOST"))
print("User:", os.getenv("DB_USER"))
print("Password:", os.getenv("DB_PASSWORD"))

try:
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user =os.getenv("DB_USER"),
        password =os.getenv("DB_PASSWORD"),
        database =os.getenv("DB_NAME")
    )
    if connection.is_connected():
        print("Successfully connected to MySQL database!")

except Error as e:
    print(f"Error while connecting to MySQl: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")