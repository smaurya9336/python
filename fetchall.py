import mysql.connector as c
mydb=c.connect(host="localhost",user="root",password="sarita",database="sarita")
cursor=mydb.cursor()
cursor.execute("select * from emp")
data=cursor.fetchall()
for i in data:
    print(i)
print("Total Number of Rows=",cursor.rowcount)
