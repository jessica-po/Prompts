from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10 ** 9)
INF = 1 << 60


MOD = 1000000007
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

pow2 = [1] * (N + 1)
for i in range(N):
    pow2[i + 1] = pow2[i] * 2 % MOD

order = []
parent = [-1] * N

stack = deque([0])
while stack:
    v = stack.pop()
    order.append(v)
    for nv in G[v]:
        if parent[v] != nv:
            parent[nv] = v
            stack.append(nv)

numer = 0
nums = [0] * N

for v in reversed(order):
    tmp = 1
    for nv in G[v]:
        if parent[v] != nv:
            nums[v] += nums[nv] + 1
            tmp += pow2[nums[nv] + 1] - 1
    tmp += pow2[N - nums[v] - 1] - 1
    numer = (numer + pow2[N - 1] - tmp) % MOD

denom = pow2[N]
ans = numer * pow(denom, MOD - 2, MOD) % MOD
print(ans)