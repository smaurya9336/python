class Test:
    college="IET LUCKNOW"
    def __init__(self):
        print("HELLO I AM FROM CONSTRUCTOR")
        self.Name="RAM"


    def demo(self): #INSTANCE METHOD
        print("NAME IS: ",self.Name)
        print("NAME IS: ",self.college)

    @classmethod
    def demo1(cls):
        print("COLLEGE NAME: ",cls.college)

    @staticmethod
    def demo2(x,y):
        print(x**y)

x=Test()
x.demo()
x.demo1()
x.demo2(10,2)