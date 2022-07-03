str1=input("string1:--")
str2=input("string2:--")


if len(str1)==len(str2):
    if sorted(str1) == sorted(str2):
        print("Given string are anagrams")
    else:
        print(" Given sentence are not anagrams")
else:
    print("given string are not anagrams")