#hierarchical INHERITANCE
class p:
    def m1(self):
        print("HELLO I AM FROM M1 METHOD PRESENT IN p parent CLASS")


class c(p):
    def m2(self):
        print("HELLO I AM FROM M2 METHOD PRESENT IN c subclass CLASS")


class d(p):
    def m3(self):
        print("HELLO I AM FROM M3 METHOD PRESENT IN d subclass CLASS")


class e(p):
    def m4(self):
        print("HELLO I AM FROM M4 METHOD PRESENT IN e subclass CLASS")

obj=c()
obj.m1()
obj.m2()
obj=d()
obj.m3()
obj.m1()
obj=e()
obj.m4()
obj.m1()

