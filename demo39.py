class test:
    def __init__(self):
        self.Name="SARITA MAURYA"
        self.Contact="9336472380"


    def msg(self):
        print("WELCOME TO TECHPILE")
        print("NAME IS: ",self.Name)
        print("Contact IS: ", self.Contact)

    def m1(self):
        self.msg()

obj=test()
obj.msg()
print(obj.Name)
print(obj.Contact)
obj.m1()