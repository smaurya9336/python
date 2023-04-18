from tkinter import *
from tkinter import messagebox
import mysql.connector as c
"""mydb=c.connect(host="localhost",user="root",password="sarita",database="login")
cursor=mydb.cursor()
while True:
    name=input("Enter User Name:")
    salary=int(input("Enter your password:"))
    query="insert into emp values('{}',{})".format(username,password)
    cursor.execute(query)
    mydb.commit()
    print("Data Inserted Successfully...")
    x=int(input("1->Enter More\n2->Exit\nEnter choice:"))
    if x==2:
        break"""
   
    
def login():
    username=entry1.get()
    password=entry2.get()

    if(username ==" " and password ==" "):
        messagebox.showinfo(" " , "Blank not allowed")

    elif(username =="sarita" and password =="12345"):
        messagebox.showinfo(" ","login success")

    else:
        messagebox.showinfo(" ","incorrect username")
        


root=Tk()
root.title("Login")
root.geometry("300x200")


global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)


entry1=Entry(root, bd=5)
entry1.place(x=140, y=20)

entry2=Entry(root, bd=5)
entry2.place(x=140, y=70)

Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()
input()


