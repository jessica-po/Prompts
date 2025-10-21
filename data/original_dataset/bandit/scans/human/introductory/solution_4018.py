def sol(a,k):
    n=len(a)
    if(k==0):return 1
    if(k==1):
        v=set()
        for x in a:
            v.add(x)
        return len(v)
    if(n<k or n<1 or k<1):
        return 0
    if(n==k):
        return 1
    sz=max(3000,n)
    v1=[0]*sz
    v2=[0]*sz
    v3=[0]*sz
    v2[n-1]=1
    v3[a[n-1]-1]=1
    for i in range(n-2,-1,-1):
        if(i<0):break
        v2[i]=v2[i+1]
        if(v3[a[i]-1]==0):
            v2[i]+=1
            v3[a[i]-1]=1
    for j in range(1,k):
        v3=[0]*sz
        v1[n-1]=0
        for i in range(n-2,-1,-1):
            v1[i]=v1[i+1]
            v1[i]=v1[i]+v2[i+1]
            v1[i] = v1[i] - v3[a[i] - 1]
            v3[a[i] - 1] = v2[i + 1]
        v2=v1.copy()
    return v1[0]
n,k=list(map(int,input().split()))
s=input()
ar=[]
for x in s:
    ar.append(ord(x))
ans=0
cur=n
while cur>=0:
    mx=min(k,sol(ar,cur))
    k-=mx
    ans+=(n-cur)*mx
    cur-=1
if(k!=0):
    print(-1)
else:
    print(ans)