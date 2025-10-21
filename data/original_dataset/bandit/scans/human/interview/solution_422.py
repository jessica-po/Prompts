def max(a, b):
	if a > b:
		return a
	else:
		return b
n, k = map(int, input().split())
x = [int(t) for t in input().split()]
y = [int(t) for t in input().split()]
f, s = 0, 0
for i in range(n):
    f = max(0, x[i] + f - k * y[i])
    s = max(0, y[i] + s - k * x[i])
    if f > k or s > k:
        print('NO')
        return
print('YES')