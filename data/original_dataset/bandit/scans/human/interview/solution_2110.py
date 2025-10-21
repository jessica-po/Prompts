import sys
import re

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

def solve():
	n, h, m, k = mints()
	m //= 2
	a = [0]*n
	e = [None]*(2*n+2)
	c = 0
	for i in range(n):
		hh, mm = mints()
		x = mm % m
		a[i] = mm
		e[2*i] = ((x+k)%m, -1, i)
		e[2*i+1] = ((x+1)%m, 1, i)
		if (x+1)%m > (x+k)%m:
			c += 1
	e[2*n] = (0,0,0)
	e[2*n+1] = (m-1,0,0)
	#print(e)
	e.sort()
	p = -1
	r = (int(1e9),0)
	#print(e)
	for x, t, id in e:
		#print(x,t,id,c)
		if p != x and p != -1:
			r = min(r, (c, p))
		p = x
		c += t
	r = min(r, (c, p))
	print(*r)
	p = r[1]
	for i in range(n):
		mm = a[i]
		x = (mm-p) % m
		if (x+1)%m > (x+k)%m and (x+k)%m != 0 \
		or (x+1)%m < (x+k)%m and (x+1)%m == 0:
			print(i+1,end=' ')


#for i in range(mint()):
solve()