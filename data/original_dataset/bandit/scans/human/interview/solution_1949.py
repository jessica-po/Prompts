(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cur = 0
idx = 0
for i in range(k):
	ans = 0
	while idx < n:
		ans = a[idx] - cur
		idx += 1
		if ans != 0:
			break
	print(ans)
	cur += ans