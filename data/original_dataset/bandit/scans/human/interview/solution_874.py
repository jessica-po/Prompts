n=int(input())

if(n%2==1):
    print(-1)

else:
    L=list(range(1,n+1))
    for i in range(0,n,2):
        t=L[i]
        L[i]=L[i+1]
        L[i+1]=t
    for i in range(n-1):
        print(L[i],end=" ")
    print(L[-1])