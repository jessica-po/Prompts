import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

n, k = mints()
q = list(mints())
for i in range(n):
	q[i] -= 1
s = list(mints())
a = [i for i in range(1,n+1)]
d = [0]*n
b = [False]*(k+1)
c = [False]*(k+1)
e = [10000]*2
f = [10000]*2
for i in range(k+1):
	#print(a)
	b[i] = (a == s)
	if b[i]:
		e[i%2] = min(e[i%2], i)
	for j in range(n):
		d[j] = a[q[j]]
	a,d = d,a
#print('====')
a = [i for i in range(1,n+1)]
for i in range(k+1):
	#print(a)
	c[i] = (a == s)
	if c[i]:
		f[i%2] = min(f[i%2], i)
	for j in range(n):
		d[q[j]] = a[j]
	a,d = d,a
#print('====')
#print(e)
#print(f)
if e[0] == 0:
	print('NO')
elif e[1] == 1:
	if f[1] == 1 and k > 1:
		print('NO')
	elif k%2 == 1 or f[k%2] <= k:
		print('YES')
	else:
		print('NO')
elif f[1] == 1:
	if k%2 == 1 or e[k%2] <= k:
		print('YES')
	else:
		print('NO')
else:
	if e[k%2] <= k or f[k%2] <= k:
		print('YES')
	else:
		print('NO')