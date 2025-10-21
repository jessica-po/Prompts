import sys
n,r,avg=list(map(int,input().split()))
L=[]
tot=0
for i in range(n):
    L.append(list(map(int,input().split())))
    L[i][0],L[i][1]=L[i][1],L[i][0]
    tot+=L[i][1]
    L[i][1]=r-L[i][1]
req=avg*n
L.sort()
ind=0
ans=0
while(ind<n and req>tot):
    diff=req-tot
    if(L[ind][1]>=diff):
        ans+=diff*L[ind][0]
        tot+=diff
        L[ind][1]-=diff
    else:
        ans+=L[ind][1]*L[ind][0]
        tot+=L[ind][1]
        L[ind][1]=0
    ind+=1
print(ans)