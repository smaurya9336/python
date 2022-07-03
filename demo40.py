class test:
    def __init__(self):
        self.__Name="SARITA MAURYA"
        self.__Contact= "9346784530"
    def __m1(self):#private member
        print("Name is: ",self.__Name)
        print("Contact is: ", self.__Contact)

    def m2(self):
        print("Name is: ",self.__Name)
        print("Contact is: ", self.__Contact)
        self.__m1()
        print("Hello I am from m2 method")


x=test()
#print(x.__Name)
#print(x.__Contact)
#x.__m1()
x.m2()
