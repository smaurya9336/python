#wap printing SARITA 
for row in range(7):
    for col in range(5):
        if(row==0 or row==3 or row==6) and (col>0 and col<4) or ((col==0) and (row>0 and row<3)) or ((col==4) and (row>3 and row<6)) or (col==0 and row==6) or (row==0 and col==4):
           print("*",end="")
        else:
            print(end=" ")
    print() 

for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#code for R
for row in range(7):
    for col in range(5):
        if(col==0) or ((row==0) or row==3) and (col>0 and col<4) or ((col==4) and (row>0 and row<3)) or (row-col==2):
            print("*",end="")
        else:
            print(end=" ")
    print()


#code for I
for row in range(7):
    for col in range(5):
        if(col==2) or ((row==0 or row==6) and (col!=2)): 
            print("*",end="")
        else:
            print(end=" ")
    print()


#code for T
for row in range(7):
    for col in range(5):
        if col==2 or (row==0 and col!=2):
            print("*",end="")
        else:
            print(end=" ")
    print()


#code for A
for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()