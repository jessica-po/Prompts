# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, edges):
    if M == N*(N-1)//2:
        return 'a' * N
    
    g = collections.defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    s = ['', 'a', 'b', 'c']
    for u in range(1, N+1):
        mark = [3 for _ in range(N + 1)]
        mark[0] = 0
        mark[u] = 1
        for v in g[u]:
            mark[v] = 1
    
        for u in range(1, N+1):
            if mark[u] == 3:
                for v in g[u]:
                    if mark[v] == 1:
                        mark[v] = 2
        
        a, b, c = mark.count(1), mark.count(2), mark.count(3)
        if a*(a-1)//2 + b*(b-1)//2 + c*(c-1)//2 + a*b + b*c != M:
            continue
        
        if any([abs(mark[u] - mark[v]) > 1 for u, v in edges]):
            continue
            
        return ''.join([s[mark[v]] for v in range(1, N+1)])
    
    return None
    

N, M = map(int, input().split())
edges = []
for i in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
    
s = solve(N, M, edges)
if s:
    print('Yes')
    print(s)
else:
    print('No')