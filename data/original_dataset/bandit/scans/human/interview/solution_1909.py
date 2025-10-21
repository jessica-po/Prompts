n,k=list(map(int,input().split()))

A=list(map(int,input().split()))
L=[]
for i in range(k):
    s=0
    for j in range(i,n,k):
        s+=A[j]
    L.append(s)

x=min(L)

print(L.index(x)+1)