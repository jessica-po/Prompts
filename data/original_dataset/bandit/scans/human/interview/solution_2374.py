#!/usr/bin/env python3
import sys
import bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
seen = set()
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
    seen.add(a)
ab.sort()

decomp = list(seen)
decomp.sort()
node_num = len(decomp)
comp = dict()
for i, item in enumerate(decomp):
    comp[item] = i

# Take diff
d = [0] * (node_num + 1)
prev = 0
for a, b in ab:
    if b != prev:
        d[comp[a]] = 1
    prev = b
if prev != 0:
    d[node_num] = 1

switch_dict = dict()
lr = []
for i in range(m):
    l, r = map(int, input().split())
    lft = bisect.bisect_left(decomp, l)
    rgt = bisect.bisect_right(decomp, r)
    if lft != rgt:
        lr.append((lft, rgt))
        switch_dict[(lft, rgt)] = i + 1

edge = [[] for _ in range(node_num + 1)]
for l, r in lr:
    edge[l].append(r)
    edge[r].append(l)

visited = [0] * (node_num + 1)
ans = []
def dfs(p, v):
    ret = d[v]
    for nv in edge[v]:
        if nv == p:
            continue
        if not visited[nv]:
            visited[nv] = 1
            val = dfs(v, nv)
            if val == 1:
                if v < nv:
                    ans.append(switch_dict[(v, nv)])
                else:
                    ans.append(switch_dict[(nv, v)])
                ret += 1
    return ret % 2

for i in range(node_num + 1):
    if visited[i]:
        continue
    visited[i] = 1
    ret = dfs(-1, i)
    # Check last node is ok or not
    if ret == 1:
        print(-1)
        return

# Check trees cover all 1 or not
for c, is_visited in zip(d, visited):
    if not is_visited and c:
        print(-1)
        return

ans.sort()
print(len(ans))
print(*ans)