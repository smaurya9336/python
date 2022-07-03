class p:
    def demo1(self): #overridden method
        print("WELCOME TO TECHPILE")
    def demo2(self):#overridden method
        print("HELLO")

class c(p):
    def demo2(self): # method overridding
        print("Hello I an from demo2 method present in p class")
    def demo1(self): #method overridding
        print("Welcome to techpile technology pvt. Ltd")
    def msg(self):
        print("HELLO I AM FROM MSG METHOD PRESENT IN C CLASS")
x=c()
x.demo1()
x.demo2()
x.msg()
