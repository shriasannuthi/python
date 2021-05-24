#sorting list using linear search
lst=[]
lim=int(input("Enter limit:"))
for i in range(0,lim):
    x=int(input())
    if x not in lst:
        lst.append(x)
for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)


#lim-1 iterations
#number of swaps is lim-i-1
            
    
        
