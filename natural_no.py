# WRITE A PROGRAM TO PRINT NATURAL NUMBERS FROM 1 TO N
from num1 import number
number=int(input("Enter any number:--"))
i=1
print("\n Natural numbers from 1 to",number)
for i in range(1,number+1):
    print(i,end=" ")


