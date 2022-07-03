#wap for fibonacci series using while loop
n=int(input("Enter a number:--"))
num1=0
num2=1
sum=0
count=1
print("Fibonacci Series:----",end="")
while(count<=n):
    print(sum)
    count=count+1
    num1=num2
    num2=sum
    sum=num1+num2
