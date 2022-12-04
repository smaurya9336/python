import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sarita",database="sakila")
if mydb.is_connected():
    print("Successfully Connected")
