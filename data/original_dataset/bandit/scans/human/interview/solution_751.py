n,m=list(map(int,input().split()))

L=list(map(int,input().split()))

ans=0

ind=0
bus=0

while(ind<n):
    ans+=1
    while(ind<n and bus+L[ind]<=m):
        bus+=L[ind]
        ind+=1
    bus=0
print(ans)