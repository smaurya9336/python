#method overloading
class test:
    def m1(self):
        print("without args method")

    def m1(self,x):
        print("1 args method")

    def m1(self,x,y):
        print("2 args method")

    def m1(self,x,y,z):
        print("3 args method")



x=test()
x.m1(10,48,40)