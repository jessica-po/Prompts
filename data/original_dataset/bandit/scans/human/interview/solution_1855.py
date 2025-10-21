n,k=map(int,input().split())
L=list(map(int,input().split()))
ind=[]
for i in range(n):
    if L[i]>n-k:ind.append(i)
m=1
for i in range(len(ind)-1):
    m*=(ind[i+1]-ind[i])
    m%=998244353
print(((n*(n+1)//2)-((n-k)*((n-k)+1))//2),m)