str1 = "SARITA"
print_S = [[" " for i in range(6)] for j in range(4)]
print_A = [[" " for i in range(6)] for j in range(4)]
#print_R= [[" " for i in range(7)] for j in range(5)]
#print_I= [[" " for i in range(7)] for j in range(5)]
#print_T= [[" " for i in range(7)] for j in range(5)]
#print_A= [[" " for i in range(7)] for j in range(5)]

#code for S
for row in range(6):
    for col in range(4):
        if(row==0 or row==3 or row==6) and (col>0 and col<4) or ((col==0) and (row>0 and row<3)) or ((col==4) and (row>3 and row<6)) or (col==0 and row==6) or (row==0 and col==4):
            print_S[row][col]= "*"

 #code for A   
for row in range(6):
    for col in range(4):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print_A[row][col]= "*"



for i in range(6):
    for j in range(4):
        print(print_S[i][j],end="")     
    print(end=" ")    
    for j in range(4):
        print(print_A[i][j],end="")     
    print()    







