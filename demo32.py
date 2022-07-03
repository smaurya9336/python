#MULTI LEVEL INHERITANCE
class p:
    def m1(self):
        print("HELLO I AM FROM M1 METHOD PRESENT IN P CLASS")


class c(p):
    def m2(self):
        print("HELLO I AM FROM M2 METHOD PRESENT IN C CLASS")


class d(c):
    def m3(self):
        print("HELLO I AM FROM M3 METHOD PRESENT IN D CLASS")


class e(d):
    def m4(self):
        print("HELLO I AM FROM M4 METHOD PRESENT IN E CLASS")

obj=c()
obj=d()
obj=e()
obj.m1()
obj.m2()
obj.m3()
obj.m4()