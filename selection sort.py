#selection sort
n=int(input("Enter the limit"))
list=[]
for k in range(0,n):
    x=int(input())
    list.append(x)
print("List before sorting",list)
for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        if(list[j]<list[min]):
            min=j
    list[i],list[min]=list[min],list[i]
    print("pass",i+1)
    for k in range(0,n):
        print(list[k],end='')
    print()
print("List after sorting",list)
