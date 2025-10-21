n=int(input())
a=list(map(int,input().split()))

lastocc=[0]*1000006
ans=[0]*n
ans[0]=1
lastocc[a[0]]=1

for i in range(1,n):
    ans[i]=ans[i-1]+(i+1-lastocc[a[i]])
    lastocc[a[i]]=i+1

print((2*sum(ans)-n)/(n*n))