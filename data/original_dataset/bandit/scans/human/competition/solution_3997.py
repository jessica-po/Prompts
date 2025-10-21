import sys
import threading
from bisect import bisect_left

n   = int(input())
a   = list(map(int, input().split()))
e   = {}
g   = [[] for i in range(n)]
d   = [0]*(n+5)
ans = [0]*n
p   = [0]*(n+5)

for i in range(n-1):
        c, w = map(int, input().split())
        c-= 1
        g[c].append(i+1)
        e[i+1] = w

def dfs(i, h):
    nonlocal ans, a, e, g, d, p
    p[h]=0
    for j in g[i]:
        d[h+1] = d[h]+e[j] 
        dfs(j, h+1)
    x = bisect_left(d, d[h]-a[i], 0, h+1)
    #print(x-1, i, h, d[h], d[h], a[i])
    if x>=0:
        p[x-1]-=1
    p[h-1]+=p[h]+1
    ans[i]=p[h]



def solve():  
    nonlocal ans
    dfs(0, 0)
    print(' '.join(map(str, ans)))

max_recur_size = 10**5*2 + 1000
max_stack_size = max_recur_size*500
sys.setrecursionlimit(max_recur_size)
threading.stack_size(max_stack_size)
thread = threading.Thread(target=solve)
thread.start()