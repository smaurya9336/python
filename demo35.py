#multiple inheritance
class test:
    def name(self,x,y):
        print("NAME is : ",x)
        print("COLLEGE is : ",y)

class test1:
    def name(self):
        print("WELCOME TO TECHPILE")

class c(test1,test):
    def demo(self):
        print("HELLO I AM FROM demo method present in c class")

x=c()
x.name()
x.demo()