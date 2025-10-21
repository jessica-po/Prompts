import sys
sys.setrecursionlimit(4100000)

mod = 10 ** 9 + 7

N, K = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = K

def factorial(n, k, mod):
    fact = 1
    for integer in range(n, n-k, -1):
        fact *= integer
        fact %= mod
    return fact

def dfs(parent, current):
    ret = 1
    for child in graph[current]:
        if child != parent:
            ret *= dfs(current, child)
    L = len(graph[current])
    R = K - 1
    if parent != -1:
        L -= 1
        R -= 1
    ret *= factorial(R, L, mod)
    return ret % mod

ans *= dfs(-1, 0)
ans %= mod

print(ans)