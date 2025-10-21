#!/usr/bin/env python3
from sys import stdin
from bisect import bisect_left, bisect_right
    
INF = int(1e9)

def find(par, a):
    if par[a] == a:
        return a
    par[a] = find(par, par[a])
    return par[a]

def union(par, rnk, a, b):
    a = find(par,a)
    b = find(par,b)
    if a==b:
        return
    
    if rnk[a]<rnk[b]:
        par[a] = b
    else:
        par[b] = a
        if rnk[a]==rnk[b]:
            rnk[a] += 1
    
def solve():
    n, m, k = map(int, stdin.readline().split())
    cnts = list(map(int, stdin.readline().split()))
    for i in range(1,k):
        cnts[i] += cnts[i-1]
    
    group = list(range(n))
    rnk = [0 for i in range(n)]
    adj = [[INF for j in range(k)] for i in range(k)]
    for i in range(m):
        u, v, x = map(int, stdin.readline().split())
        if x==0:
            union(group, rnk, u-1, v-1)
        tu = bisect_left(cnts, u)
        tv = bisect_left(cnts, v)
        adj[tu][tv] = min(adj[tu][tv], x)
        adj[tv][tu] = min(adj[tv][tu], x)
    
    p = 0
    for i in range(k):
        cur = group[p]
        while p<cnts[i]:
            if group[p]!=cur:
                print("No")
                return
            p += 1
    print("Yes")
    
    for p in range(k):
        for i in range(k):
            for j in range(k):
                adj[i][j] = min(adj[i][j], adj[i][p]+adj[p][j])
    
    for i in range(k):
        adj[i][i] = 0
        for j in range(k):
            if adj[i][j] == INF:
                adj[i][j] = -1
    
    for i in range(k):
        print(' '.join(map(lambda x: str(x), adj[i])))
    
    
solve()