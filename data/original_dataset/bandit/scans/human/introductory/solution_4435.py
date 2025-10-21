from heapq import heappush, heappop

n = int(input())
a = list(map(int, input().split()))
edge = [[] for _ in range(n)]
rev = [[] for _ in range(n)]
inf = 10**9
cost = [inf]*n
hq = []

for i, x in enumerate(a):
    if i+x < n:
        edge[i].append(i+x)
        rev[i+x].append(i)
        if (a[i] ^ a[i+x]) & 1:
            cost[i] = 1
    if i-x >= 0:
        edge[i].append(i-x)
        rev[i-x].append(i)
        if (a[i] ^ a[i-x]) & 1:
            cost[i] = 1

    if cost[i] == 1:
        hq.append((1, i))

while hq:
    c, v = heappop(hq)
    if cost[v] < c:
        continue
    c += 1
    for dest in rev[v]:
        if cost[dest] > c:
            cost[dest] = c
            heappush(hq, (c, dest))

for i in range(n):
    if cost[i] == inf:
        cost[i] = -1

print(*cost)