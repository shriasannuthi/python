#to print fibonacci series
n=int(input("Enter a number: "))
a=0
b=1
print(a)
print(b)
for c in range (1,n+1):
    c=a+b
    a=b
    b=c
    print(c)
