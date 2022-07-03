from math import factorial;
class calc:
    def add(self, x,y=100):
         print("SUM IS: ",x+y)

    def mul(self,x=30,y=10):
         print("MUL IS: ",x*y)

    def listsum(self):
        list=[10,20,30,40,50]
        sum=0
        for x in list:
            sum=sum+x

        print("LIST SUM: ",sum)

    def fact(self,x=4):
        print("Factorial of: ",x,"is:",factorial(x))

        obj=calc()
        obj.add(10)
        obj.mul(10,80)
        obj.mul()
        obj.listsum()
        obj.fact(10)
        obj.fact()