n, m = map(int, input().split())
d = []
for i in range(n):
	d.append(list(map(int, input().split())))
k = 0
for i in d:
	if i[0] <= k:
		k = max(k, i[1])
if k >= m:
	print('YES')
else:
	print('NO')