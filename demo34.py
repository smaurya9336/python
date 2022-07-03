# this is MULTIPLE INHERITANCE
class p1:
    def m1(self):
        print("HELLO I AM FROM  M1 METHOD present in p1 class")

class p2:
    def m2(self):
        print("HELLO I AM from M2 METHOD present in p2 class")

class p3:
    def m3(self):
        print("HELLO I AM from M1 METHOD present in p3 class")

class c(p1,p2,p3):
    def m4(self):
        print("HELLO I am from m4 method present in c class")

obj=c()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
