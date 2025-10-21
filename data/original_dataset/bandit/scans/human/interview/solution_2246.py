from sys import stdin
from decimal import Decimal as D
input = stdin.readline
n = int(input())
adj = [[] for i in range(n+1)]
tree = [[] for i in range(n+1)]
visit = [-1]*(n+1)
length = [-1]*(n+1)
for i in range(n-1):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
bfsord = []

from collections import deque
Q = deque()
Q.append(1)
visit[1] = 0
while len(Q):
    p = Q.popleft()
    bfsord.append(p)
    for q in adj[p]:
        if visit[q] != -1: continue
        visit[q] = visit[p]+1
        Q.append(q)
        tree[p].append(q)

for p in reversed(bfsord):
    if not tree[p]: length[p] = D(0)
    else: length[p] = D(1) + sum(length[q] for q in tree[p])/len(tree[p])
print(length[1])