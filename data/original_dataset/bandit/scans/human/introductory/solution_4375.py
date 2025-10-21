n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
g = {}

def dfs(v, p=-1):
	c = [dfs(child, v) for child in g.get(v, set()) - {p}]
	c.sort(key=len, reverse=True)
	r = []
	i = 0
	while c:
		if i >= len(c[-1]):
			c.pop()
		else:
			o = max(i, k - i - 1)
			s = q = 0
			for x in c:
				if len(x) <= o:
					q = max(q, x[i])
				else:
					s += x[o]
					q = max(q, x[i] - x[o])
			r.append(q + s)
			i += 1
	r.append(0)
	for i in range(len(r) - 1, 0, -1):
		r[i - 1] = max(r[i - 1], r[i])
	while len(r) > 1 and r[-2] == 0:
		r.pop()
	o = (r[k] if k < len(r) else 0) + a[v]
	r.insert(0, max(o, r[0]))
	return r


for _ in range(1, n):
	u, v = [int(x) - 1 for x in input().split()]
	g.setdefault(u, set()).add(v)
	g.setdefault(v, set()).add(u)

print(dfs(0)[0])