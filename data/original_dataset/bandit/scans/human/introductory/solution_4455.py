def ke(i):
    return a[i]
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(i)
b.sort(key=ke)
ans=[0]*n
k=0
for i in range(1,n):
    if a[b[i]]==a[b[i-1]]:
        k+=1
        ans[b[i]]=i-k
    else:
        k=0
        ans[b[i]]=i
for i in range(m):
    r1,r2=map(int,input().split())
    if (a[r1-1]>a[r2-1]):
        ans[r1-1]-=1
    elif a[r1-1]<a[r2-1]:
        ans[r2-1]-=1
for i in ans:
    print(i, end=' ')