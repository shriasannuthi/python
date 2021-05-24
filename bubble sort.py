#bubble sort
n=int(input("Enter the limit"))
list=[]
for k in range(0,n):
    x=int(input())
    list.append(x)
print("List before sorting ",list)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(list[j]>list[j+1]):
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
    print("pass",i+1)
    for k in range(0,n):
        print(list[k],end='')
    print()
print("List after sorting",list)
