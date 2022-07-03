#write a program to check a string is palindrome or not
import string

string=input("Enter a String:--")
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("String is not a palindrome")