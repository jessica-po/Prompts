def read_ints():
	return [int(i) for i in input().split()]

n, k, t = read_ints()
if t <= k:
	print(t)
elif t > n:
	print(k + n - t)
else:
	print(k)