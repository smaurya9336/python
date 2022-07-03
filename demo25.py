class Test:
    def __init__(self):
        self.Name="TECHPILE" #instance variable
        self.Userid="TPTST123"
        print("HELLO I AM PRESENT IN CONSTRUCTOR")
    def demo(self):
        print("I AM PRESENT IN DEMO FUNCTION")


x=Test()
x.__init__()#constructor
x.demo()