n = int(input())
graph = [set() for tr in range(n+2)]
i = 1
while i < n:
	x, y = list(map(int, input().split()))
	graph[x].add(y)
	graph[y].add(x)
	i += 1
a = iter(map(int, input().split()))
try:
	assert next(a) == 1
	q = [1]
	for v in q:
		gv = graph[v]
		gv1 = tuple(gv)
		for tr2 in gv1:
			u = next(a)
			assert u in gv
			gv.remove(u)
			graph[u].remove(v)
			q.append(u)
	print("Yes")
except AssertionError:
	print("No")