#to print floyd triangle
'''1
23
456
78910'''
n=int(input("Enter a limit"))
for i in range(1,n+1):
    print(i,end=' ')
    for j in range(1,i+1):
        if (j==i):
            print()
        
