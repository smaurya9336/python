#write a program to check inputed number is prime number or not
num=int(input("Enter any number:--"))
if num>1:
    for i in range(2,num):
        if(num%2==0):
            print(num,"is not a prime number")

        else:
            print(num,"is a prime number")

else:
    print(num,"is not a prime number")