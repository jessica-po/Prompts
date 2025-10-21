mod = 998244353

n = int(input())

a = list(map(int, input().split()))

d = {}

for i in range(n):
	if a[i] not in d:
		d[a[i]] = (i, i)
	else:
		d[a[i]] = (d[a[i]][0], i)

d2 = {}

for k, v in list(d.items()):
	if v[0] != v[1]:
		d2[k] = v

active, ans = 0, 1

for i in range(n - 1):
	if a[i] in d2:
		if i == d2[a[i]][0]:
			active += 1
		if i == d2[a[i]][1]:
			active -= 1
	if active == 0:
		ans = (ans * 2) % mod

print(ans)