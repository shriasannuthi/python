#to find if a number is a strong number
n=int(input())
cpy=n
sum=0
while(n>0):
    m=n%10
    n=n//10
    fact=1
    while(m>0):
            fact=fact*m
            m=m-1
    sum=sum+fact
if(sum==cpy):
    print("The number is a strong number")
else:
    print("The number is not a strong number")
