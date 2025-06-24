import mysql.connector
from mysql.connector import Error

#Connect to MySQl database
def connect_to_db():
    return mysql.connector.connect(
            host="localhost",
            user="philip",
            password="Worldw@rz700#",
            database="library_database"
    )
    
#Create books table (Run once)
def create_books_table():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            isbn VARCHAR(50)
        )
    """)
    mydb.commit()
    mycursor.close()
    mydb.close()

#Function to add a book
def add_book(title, author, isbn):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
    val = (title, author, isbn)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Book {title} added successfully")
    mycursor.close()
    mydb.close()

#Function to search for a book by title
def search_book(title):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM books WHERE title LIKE %s"
    val = ("%" + title + "%",)
    mycursor.execute(sql, val)
    results = mycursor.fetchall()

    if results:
        print("Matching books:")
        for book in results:
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | ISBN: {book[3]}")
        else: 
            print("No books found with that title")
        mycursor.close()
        mydb.close()
search_book("Atomic")

#Function to list all books
def list_books():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM books")
    results = mycursor.fetchall()
    print("All Books:")
    for book in results:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} ISBN: {book[3]}")
    mycursor.close()
    mydb.close()
list_books()

#Function to delete book by ID
def delete_book(book_id):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "DELETE FROM books WHERE id = %s"
    val = (book_id,)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount > 0:
            print(f"Book with ID {book_id} deleted successfully.")
        else:
            print(f"No book found with ID {book_id}") 
    except mysql.connector.Error as err:
        print(f"Error {err}")  
    finally:
        mycursor.close()
        mydb.close()
  
delete_book(3)


