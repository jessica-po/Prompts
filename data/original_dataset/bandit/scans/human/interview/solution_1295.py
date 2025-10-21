from bisect import *

n, m = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

r = -1

a.sort()
b.sort()

for i in a:
	y = 1000000000000
	x = bisect_left(b, i)
	if (x >= 0) and (x < m):
		y = min(y, abs(i - b[x]))
	x += 1
	if (x >= 0) and (x < m):
		y = min(y, abs(i - b[x]))
	x -= 2
	if (x >= 0) and (x < m):
		y = min(y, abs(i - b[x]))
	r = max(r, y)

print(r)