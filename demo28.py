class Testdemo:
    College="IET LUCKNOW" #static variable
    def __init__(self,name,contact):
        print("WELCOME TO PARAMETERISE CONSTRUCTOR")
        print("*"*30)
        self.Name=name #instance variavle
        self.Contact=contact #instance variable


    def info(self):
        print("NAME IS:",self.Name)
        print("CONTACT NO IS:", self.Contact)
        print("COLLEGE NAME IS:", self.College)

    def demo(self):
        sum=0
        for x in range(1,5):
            sum=sum+x
            print(sum)

obj=Testdemo("RAM","4000678899")
obj.info()
x=Testdemo("SYAM","6667788888")
x.info()
x.demo()




