class Testdemo:
    def __init__(self,name,contact,college):
        print("WELCOME TO PARAMETRISE CONSTRUCTOR")
        print("*"*30)
        self.Name=name
        self.Contact=contact
        self.College=college

    def info(self):
        print("NAME IS:",self.Name)
        print("CONTACT NO IS:", self.Contact)
        print("COLLEGE NAME IS:", self.College)

"""a=Testdemo("RAHUL","56678889999","ASSJHH")
a.info() """

n=input("ENTER YOUR NAME: ")
c=input("ENTER YOUR CONTACT NO : ")
clg=input("ENTER YOUR COLLEGE NAME: ")
a=Testdemo(n,c,clg)
a.info()
x=Testdemo(n,c,clg)
x.info()
