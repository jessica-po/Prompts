X,n=list(map(int,input().split()))


Taken=[True]*(X+1)
for i in range(n):
    x=list(map(int,input().split()))
    if(x[0]==1):
        Taken[x[1]]=False
        Taken[x[2]]=False
    else:
        Taken[x[1]]=False
cnt=0
minn=0
maxx=0
ans=0
for i in range(1,X):
    if(Taken[i]):
        cnt+=1
        maxx+=1
    else:
        ans+=cnt//2
        if(cnt%2!=0):
            ans+=1
        cnt=0
ans+=cnt//2
if(cnt%2!=0):
    ans+=1
print(ans,maxx)