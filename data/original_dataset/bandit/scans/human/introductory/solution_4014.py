def ke(i):
    return b[i]
n,m=map(int,input().split())
a=[0]*m
b=[0]*m
c=[0]*m
e=[]
ans=[0]*n
for i in range(m):
    a[i],b[i],c[i]=map(int,input().split())
    ans[b[i]-1]=m+1
    e.append(i)
e.sort(key=ke)
for i in range(m):
    k=0
    for j in range(a[e[i]]-1,b[e[i]]-1):
        if ans[j]==0:
            ans[j]=e[i]+1
            k+=1
        if k==c[e[i]]:
            break
    if k!=c[e[i]]:
        print(-1)
        return
for i in ans:
    print(i,end=' ')