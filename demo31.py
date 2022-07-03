class p:
    def m1(self):
        print("Hello I am  from m1 method present in p class ")

#SINGLE INHERITANCE
class c(p):
    def m2(self):
        print("Hello I am from m2 method present in c class")
obj=c()
obj.m1()
obj.m2()
