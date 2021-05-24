#armstrong numbers are numbers whose digits are raise to the power of number of digits
a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
for i in range(a,b+1):
    sum=0
    temp=i
    while(temp>0):
        n=temp%10
        sum=sum+n**3
        temp=temp//10
        if(i==sum):
            print(i)
