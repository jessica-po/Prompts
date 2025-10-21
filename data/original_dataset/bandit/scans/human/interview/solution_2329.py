import  sys
input=sys.stdin.readline
n,m=list(map(int,input().split()))
a=[int(x) for x in input().split()]
s=[set() for i in range(m+1)]

for i in range(n):
    s[a[i]].add(i+1)

f=[0]*(m+2)
for i in range(m+1):
    f[i]=i

def fin(x):
    if f[x]==x:
        return x
    f[x]=fin(f[x])
    return f[x]
ans=0
for i in range(1,m+1):
    for j in s[i]:
        if j in s[i] and j-1 in s[i]:
            ans+=1

out=[n-ans-1]

for i in range(m-1):
    x,y=list(map(int,input().split()))
    x=fin(x)
    y=fin(y)

    if len(s[x])<len(s[y]):
        x,y=y,x
    for i in s[y]:
        if i in s[y] and i-1 in s[x]:
            ans+=1
        if i in s[y]  and i+1 in s[x]:
            ans+=1

    out.append(n-ans-1)
    s[x]|=s[y]
    f[y]=x

print('\n'.join(str(x) for x in out))