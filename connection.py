import mysql.connector

# Connection Establishment
try:
    # Creating connection object
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin"
    )
    print(mydb)
    print("Connection successful")

    # Database Creation
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS BSCCS")
    print("Database created")

    # Display Databases
    mycursor.execute("SHOW DATABASES")
    print("Databases:")
    for x in mycursor:
        print(x)

    # Switch to the created database
    mycursor.execute("USE BSCCS")

    # Table Creation
    mycursor.execute("CREATE TABLE IF NOT EXISTS student (name VARCHAR(25), Regno VARCHAR(50), Total INT, Grade CHAR(1))")
    print("Table created")

    # Display Tables
    mycursor.execute("SHOW TABLES")
    print("Tables:")
    for x in mycursor:
        print(x)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("Connection closed")
