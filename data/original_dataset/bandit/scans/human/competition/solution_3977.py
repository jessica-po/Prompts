def cin():
    return list(map(int, input().split()))

def dfs(n):
    if not C[n]:
        C[n]=True
        s[0]+=1
    for i in B[n]:
        if not C[i]:dfs(i)

n,m,k=cin()
A=cin()
A=[i-1 for i in A]
B=[list([]) for i in range(n)]
C=[False for i in range(n)]
ans=mx=0
for i in range(m):
    a,b=[i-1 for i in cin()]
    B[a].append(b)
    B[b].append(a)

for i in range(k):
    s=[0]
    dfs(A[i])
    ans+=s[0]*(s[0]-1)//2
    mx=max(mx,s[0])

ans-=mx*(mx-1)//2
for i in range(n):
    if not C[i]:
        s=[0]
        dfs(i)
        mx+=s[0]

print(ans-m+mx*(mx-1)//2)