import mysql.connector
from mysql.connector import Error

try :
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Alx#2025"
        # database = "md_water_services"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print(f"Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
        print(mysql.connector.Error)

finally:
     # Close the cursor if it exists
    if mycursor in locals() and mycursor:
        mycursor.close()
    # Close the connection if it exists and is still open
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()




""" 

    # mycursor.close()
    mydb.close()

myresult = mycursor.fetchall() 

for rows in myresult[:5]:
    print(rows)

print(f"Database 'alx_book_store' created successfully!")"""


