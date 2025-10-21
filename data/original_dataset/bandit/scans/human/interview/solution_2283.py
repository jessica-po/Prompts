from collections import deque

def addedge(u, v, value):
	nonlocal e
	a = [v, value, None]
	b = [u, 0, a]
	a[2] = b
	e[u].append(a)
	e[v].append(b)
	

inf = 2 * (10 ** 12)
ans = 0
n, m = list(map(int, input().split()))
e = [[] for i in range(n + m + 2)]
a = tuple(map(int, input().split()))
S, T = 0, m + n + 1
for i in range(1, m + 1):
	u, v, w = list(map(int, input().split()))
	ans += w
	addedge(i, u + m, inf)
	addedge(i, v + m, inf)
	addedge(S, i, w)
for i in range(m + 1, T):
	addedge(i, T, a[i - m - 1])
# for i in range(n + m + 2):
# 	for edge in e[i]:
# 		print('%d to %d w %d' % (i, edge[0] if edge[0] <= m else edge[0] - m, edge[1]))

lvl = None
def bfs():
	nonlocal e, lvl
	lvl = [0] * (n + m + 2)
	q = deque([0])
	while q:
		node = q.popleft()
		# print('node = %d' % node)
		for edge in e[node]:
			if edge[0] != 0 and lvl[edge[0]] == 0 and edge[1]:
				lvl[edge[0]] = lvl[node] + 1
				q.append(edge[0])
	# print(lvl)


def dfs(node, maxdelta):
	nonlocal e, lvl
	if node == T:
		return maxdelta
	delta = 0
	for edge in e[node]:
		if lvl[edge[0]] == lvl[node] + 1 and edge[1]:
			tmp = dfs(edge[0], min(maxdelta, edge[1]))
			if tmp > 0:
				edge[1] -= tmp
				edge[2][1] += tmp
				maxdelta -= tmp
				delta += tmp
			if maxdelta == 0:
				break
	return delta

flow = 0
while 1:
	bfs()
	tmp = dfs(0, inf)
	if tmp == 0:
		break
	flow += tmp
ans -= flow
print(ans)