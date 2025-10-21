import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

n, k, x = mints()
a = list(mints())
d = [None]*(n+1)
p = [None]*(n+1)
for i in range(0,k):
	d[i] = a[i]
for xx in range(2,x+1):
	d,p = p,d
	for nn in range(n):
		m = None
		for i in range(max(0,nn-k),nn):
			if p[i] != None:
				if m == None:
					m = p[i]
				else:
					m = max(m, p[i])
		if m != None:
			d[nn] = m + a[nn]
		else:
			d[nn] = None
m = -1
for i in range(n-k,n):
	if d[i] != None:
		m = max(m, d[i])
print(m)