import mysql.connector as c
mydb=c.connect(host="localhost",user="root",password="sarita",database="sarita")
cursor=mydb.cursor()
cursor.execute("select * from emp")
data=cursor.fetchone()
print(data)
record=cursor.rowcount
print("Total Number of Rows=",record)
