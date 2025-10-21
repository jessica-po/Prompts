n,m=list(map(int,input().split()))
M=[[] for i in range(n)]
for i in range(m):
    a,b=list(map(int,input().split()))
    a-=1;b-=1
    M[a].append(b)
    M[b].append(a)
yes="POSSIBLE";no="IMPOSSIBLE"

for i in M[0]:
    if n-1 in M[i]:
        print(yes);return
print(no)