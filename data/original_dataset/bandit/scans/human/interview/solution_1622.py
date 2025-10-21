n, m = map(int, input().split())
ev = [tuple(map(int, input().split())) for _ in range(m)]

g = [[] for _ in range(n + 1)]
qry = [[] for _ in range(m + 1)]
roots = set(range(1, n + 1))
qcnt = 0
for e in ev:
	if e[0] == 1:
		g[e[2]].append(e[1])
		roots.remove(e[1])
	elif e[0] == 3:
		qry[e[2]].append((qcnt, e[1]))
		qcnt += 1

tin, tout = [0] * (n + 1), [0] * (n + 1)
st = [(u, 0) for u in roots]
time = 0
while st:
	u, w = st.pop()
	if w:
		tout[u] = time
		continue
	time += 1
	tin[u] = time
	st.append((u, 1))
	for v in g[u]:
		st.append((v, 0))

p = list(range(n + 1))
def find(x):
	if x != p[x]:
		p[x] = find(p[x])
	return p[x]

pcnt = 0
ans = [None] * qcnt
for e in ev:
	if e[0] == 1:
		p[find(e[1])] = find(e[2])
	elif e[0] == 2:
		pcnt += 1
		for qid, x in qry[pcnt]:
			ans[qid] = 'YES' if find(e[1]) == find(x) and tin[x] <= tin[e[1]] <= tout[x] else 'NO'

print(*ans, sep='\n')