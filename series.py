def sumofSeries(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i*i*i
    return sum
n=int(input("enter any number:--"))
print("sum of series:",sumofSeries(n))

    
