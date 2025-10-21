s, r = map(int, input().split())
v = []
for i in range(s):
	v += [list(map(int, input().split()))]
ans = 0
p = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(s):
	if v[i].count(1) == 0:
		continue
	if v[i].count(1) == 1:
		ans += r - 1
	else: 
		a = v[i].index(1)
		b = v[i][::-1].index(1)
		ans += 2 * r - a - b - 2 * v[i].count(1)
v1 = []
for i in range(r):
	v1 += [[v[j][i] for j in range(s)]]
for i in range(r):
	if v1[i].count(1) == 0:
		continue
	if v1[i].count(1) == 1:
		ans += s - 1
	else: 
		a = v1[i].index(1)
		b = v1[i][::-1].index(1)
		ans += 2 * s - a - b - 2 * v1[i].count(1)
print(ans)