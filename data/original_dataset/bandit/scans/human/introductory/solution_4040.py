from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,M,d = inpl()
CC = inpl()

if sum(CC) + (d-1)*(M+1) < N:
    print("NO")
else:
    x = 0
    ans = [0]*(d-1)
    i = 0
    for i in range(M):
        ans += [i+1] * CC[i]
        ans += [0] * (d-1)

    L = len(ans) - N
    ans2 = []
    for a in ans:
        if a == 0 and L > 0:
            L -= 1
        else:
            ans2.append(a)

    print("YES")
    print(" ".join(map(str,ans2)))