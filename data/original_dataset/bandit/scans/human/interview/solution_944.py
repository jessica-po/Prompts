import sys
import threading
from collections import defaultdict

def put():
    return map(int, input().split())

def dfs(i, p, m):
    cnt = 1
    z = 0
    for j in tree[i]:
        if j==p: continue
        if cnt==m: cnt+=1
        index = edge_index[(i,j)]
        ans[cnt].append(index)
        z = max(dfs(j,i,cnt), z)
        cnt+=1
    return max(z,cnt-1)

def solve():
    l = dfs(1,0,0)
    print(l)
    for i in range(1, l+1):
        print(len(ans[i]), *ans[i])
    

n = int(input())
edge_index = defaultdict()
ans = [[] for i in range(n+1)]
tree = [[] for i in range(n+1)]
for i in range(n-1):
    x,y = put()
    edge_index[(x,y)]=i+1
    edge_index[(y,x)]=i+1
    tree[x].append(y)
    tree[y].append(x)

max_recur_size = 10**5*2 + 1000
max_stack_size = max_recur_size*500
sys.setrecursionlimit(max_recur_size)
threading.stack_size(max_stack_size)
thread = threading.Thread(target=solve)
thread.start()