import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def add(a,x,v):
	while x<len(a):
		a[x] += v
		x |= x+1
def get(a,x):
	r = 0
	while x>=0:
		r += a[x]
		x = (x&(x+1))-1
	return r


n, k, a, b, q = mints()
h1 = [0]*n
h2 = [0]*n
z = [0]*n
for i in range(q):
	t = tuple(mints())
	if t[0] == 1:
		p = z[t[1]-1]
		pp = p + t[2]
		add(h1, t[1]-1, min(a,pp)-min(a,p))
		add(h2, t[1]-1, min(b,pp)-min(b,p))
		z[t[1]-1] = pp
	else:
		print(get(h2,t[1]-2)+get(h1,n-1)-get(h1,t[1]+k-2))