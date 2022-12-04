import mysql.connector as c
mydb=c.connect(host="localhost",user="root",password="sarita",database="sarita")
cursor=mydb.cursor()
while True:
    id=int(input("Enter Employee Id:"))
    name=input("Enter Employee Name:")
    desig=input("Enter Employee Designation:")
    salary=int(input("Enter Employee Salary:"))
    query="insert into emp values({},'{}','{}',{})".format(id,name,desig,salary)
    cursor.execute(query)
    mydb.commit()
    print("Data Inserted Successfully...")
    x=int(input("1->Enter More\n2->Exit\nEnter choice:"))
    if x==2:
        break
