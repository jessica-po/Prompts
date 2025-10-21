#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ford_fulkerson:
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev
        
        def __repr__(self):
            return "to : {0} cap : {1} rev : {2}".format(self.to, self.cap, self. rev)

    def __init__(self,V):
        self.V = V
        self.size = [0 for i in range(V)]
        self.G = [[] for i in range(V)]

    def add_edge(self, _from, to, cap):
        self.size[_from]
        self.G[_from].append(self.Edge(to, cap, self.size[to]))
        self.G[to].append(self.Edge(_from, 0, self.size[_from]))
        self.size[_from] += 1
        self.size[to] += 1

    def dfs(self, v, t, f):
        if v == t: return f
        self.used[v] = True
        for i in range(len(self.G[v])):
            edge = self.G[v][i]
            if self.used[edge.to] is False and edge.cap > 0:
                d = self.dfs(edge.to, t, f if f < edge.cap else edge.cap)
                if d > 0:
                    self.G[v][i].cap -= d
                    self.G[edge.to][edge.rev].cap += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.used = [False for _ in range(self.V)]
            f = self.dfs(s, t, float('inf'))
            if f == 0:
                return flow
            flow += f

N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ff = ford_fulkerson(N*2+2)
S = 1
T = N + 1

for i in range(M):
    p,q = list(map(int, input().split()))
    ff.add_edge(p,T+q-1,10**9)
    ff.add_edge(q,T+p-1,10**9)

for i in range(N):
    ff.add_edge(i+1,T+i,10**9)
    ff.add_edge(0,S+i,A[i])
    ff.add_edge(T+i,2*N+1,B[i])

ans = [[0  for i in range(N)] for j in range(N)]
ff.max_flow(0,2*N+1)

for i in range(1,N+1):
    for v in ff.G[i]:
        if v.to != 0:
            ans[i-1][v.to-T] = ff.G[v.to][v.rev].cap

if M == 0:
    if A == B:
        print('YES')
        for i in range(N):
            for j in range(N):
                ans [i][j] = A[i] if i == j else 0
        for a in ans:
            print(' '.join(map(str,a)))
    else:
        print('NO')
else:
    if [sum([ans[i][j] for i in range(N)]) for j in range(N)] == B:
        print('YES')
        for a in ans:
            print(' '.join(map(str,a)))
    else:
        print('NO')