from queue import Queue
import sys

cost = []

def readarray(): return list(map(int, input().split(' ')))

n = int(input())
graph = [[] for i in range(n)]

for i in range(n - 1):
	u, v, c = readarray()
	u, v = u - 1, v - 1
	cost.append(c)
	graph[u].append((v, i))
	graph[v].append((u, i))
	

order = []
used = [0] * n
q = [0] * (n + n)

qh = qt = 0


used[qh] = 1
qh += 1

while qt < qh:
	v = q[qt]
	qt += 1
	
	order.append(v)
	
	for (to, e) in graph[v]:
		if used[to]:
			continue
		used[to] = 1
		q[qh] = to
		qh += 1
		

		
order.reverse()
		
sz = [0 for x in range(n)]

for v in order:
	sz[v] = 1
	for (to, e) in graph[v]:
		sz[v] += sz[to]
"""

sz = [0] * n

sys.setrecursionlimit(100505)

def dfs(v, p):
	sz[v] = 1
	
	for (to, e) in graph[v]:
		if to != p:
			dfs(to, v)
			sz[v] += sz[to]
			
dfs(0, -1)

"""

distanceSum = 0.0
edgeMult = [0] * n

for v in range(n):
	for (to, e) in graph[v]:
		x = min(sz[v], sz[to])
		edgeMult[e] = x
		distanceSum += 1.0 * cost[e] * x * (n - x)
		
distanceSum /= 2.0

queryCnt = int(input())

ans = []

for i in range(queryCnt):
	x, y = readarray()
	x -= 1
	
	distanceSum -= 1.0 * cost[x] * edgeMult[x] * (n - edgeMult[x])
	cost[x] = y
	distanceSum += 1.0 * cost[x] * edgeMult[x] * (n - edgeMult[x])
	
	ans.append('%.10lf' % (distanceSum / n / (n - 1) * 6.0))

print('\n'.join(ans))