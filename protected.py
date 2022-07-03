class test:
    def __init__(self):
        self._Name="SARITA MAURYA"
        self._Contact = "9336472380"
    def _m1(self):
        print("Name is:",self._Name)
        print("Contact is:", self._Contact)


    def m2(self):
        print("Hello I am from m2 method present in test parent class")
        self._m1()

class c(test):
    def demo(self):
        print(self._Name)
        print(self._Contact)
        self._m1()


x=c()
x.demo()
y=test()
y._m1()