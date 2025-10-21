from collections import deque

n = int(input())
p = list(map(int,input().split()))
a = list(map(int,input().split()))
edge = [[] for i in range(n)]
for i in range(n-1):
    edge[p[i]-1].append(i+1)


dp = [0 for i in range(n)]
size = [not edge[v] for v in range(n)]

res = []
deq = deque([0])
while deq:
    v = deq.popleft()
    res.append(v)
    for nv in edge[v]:
        deq.append(nv)

res = res[::-1]

for v in res:
    tmp = -1
    S = 0
    for nv in edge[v]:
        tmp = max(tmp,dp[nv])
        size[v] += size[nv]
        S += a[nv]

    if not edge[v]:
        dp[v] = a[v]
        continue

    rest = tmp*size[v] - S
    if a[v]<=rest:
        dp[v] = tmp
    else:
        q = (a[v]-rest)//size[v]
        r = (a[v]-rest)%size[v]
        if r:
            dp[v] = tmp + q + 1
        else:
            dp[v] = tmp + q
    a[v] += S

print(dp[0])