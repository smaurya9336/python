#write a program to print fibonaaci series in python
num=int(input("Enter a number:--"))
num1=0
num2=1
sum=0
count=1
print("Fibonacci series:--",end="")
while(count<=num):
    print(sum)
    count=count+1
    num1=num2
    num2=sum
    sum=num1+num2
