#write a program to print a number is palindrome or not?
num=int(input("Enter a Number:"))
temp=num
RevNum=0
while(num>0):
    Rem=num%10
    RevNum=RevNum*10+Rem
    num=num//10
if(temp==RevNum):
    print("The number is palindrome!")

else:
    print("Not a Palindrome!")

