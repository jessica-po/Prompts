import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

n, m = mints()
a = list(minp())
x = 0
t = 0
d = 1
for i in range(n-1):
	b = list(minp())
	l = x
	r = x
	wall = 0
	while True:
		t += 1
		if b[x] == '.':
			break
		if x + d == m or x + d < 0 or a[x+d] == '#':
			wall += 1
			d = -d
			if wall == 2:
				print("Never")
				return
		elif a[x+d] == '+':
			wall = 0
			a[x+d] = '.'
			d = -d
		elif l <= x+d and x+d <= r:
			if d == 1:
				t += r-x-1
				x = r
			else:
				t += x-l-1
				x = l
		else:
			x += d
			r = max(r,x)
			l = min(l,x)
	a, b = b, a
print(t)