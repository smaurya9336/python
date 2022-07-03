x=10#global variable
def fun1():
    a=10 #local variable
    print(x)
    global y
    y=True

fun1()

def fun2():
    print(x)
    print(y)

fun2()