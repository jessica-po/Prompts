import sys

n, k = (int(i) for i in input().split())

ff = [1] * (n + 1)

for i in range(1, n + 1) :
	ff[i] = ff[i - 1] * i

dd = [0] * (n + 1)

dd[1] = 0
dd[2] = 1

for i in range(3, n + 1) :
	dd[i] = (i - 1) * (dd[i - 1] + dd[i - 2])
	
ans = ff[n]

for i in range(n - k) :
	c = ff[n] // ff[n - i]
	c = c // ff[i]
	c = c * dd[n - i]
	
	ans -= c

print(ans)