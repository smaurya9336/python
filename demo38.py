class test:
    def fdiv(self,x,y):#overridden method
        print("Result is: ",x/y)

    def add(self,x,y,z):#overridden method
        print("Sum is: ",(x+y+z))



class c(test):
    def fdiv(self,x,y,z):#method overridding
        print("Multiplication is: ",(x*y*z))
    def __init__(self):
       print("==== WElocme to techpile====")
    def add(self,a,b,c,d):#method overridding
        print("Result is: ",(a+b+c+d))

x=c()
x.fdiv(10,2,5)
x.add(10,6,40,5)