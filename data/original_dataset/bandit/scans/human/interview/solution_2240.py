import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

def add(a,b):
	return (a+b)%1000000007

def sub(a,b):
	return (a+1000000007-b)%1000000007

def mul(a,b):
	return (a*b)%1000000007

p = 102367
s = list(map(int,minp()))
t = list(map(ord,minp()))
h = [0]*(len(t)+1)
pp = [1]*(len(t)+1)
for i in range(len(t)):
	h[i+1] = add(mul(h[i], p), t[i])
	pp[i+1] = mul(pp[i], p)

def cmp(a, b, l):
	if a > b:
		a, b = b, a
	h1 = sub(h[a+l], mul(h[a], pp[l]))
	h2 = sub(h[b+l], mul(h[b], pp[l]))
	return h2 == h1

c = [0,0]
idx = [-1,-1]
for i in range(len(s)):
	c[s[i]] += 1
	if idx[s[i]] < 0:
		idx[s[i]] = i
Mv = max(c)
mv = min(c)
Mi = c.index(Mv)
mi = (Mi^1)
lt = len(t)
sp = [0,0]
res = 0
for k in range(1,lt//Mv+1):
	l = [0,0]
	x = (lt-k*Mv)//mv
	if x > 0 and x*mv + k*Mv == lt:
		l[Mi] = k
		l[mi] = x
		if idx[0] < idx[1]:
			sp[0] = 0
			sp[1] = idx[1]*l[0]
		else:
			sp[1] = 0
			sp[0] = idx[0]*l[1]
		ok = True
		j = 0
		for i in range(len(s)):
			if not cmp(sp[s[i]], j, l[s[i]]):
				ok = False
				break
			j += l[s[i]]
		if l[0] == l[1] and cmp(sp[0], sp[1], l[0]):
			ok = False
		if ok:
			res += 1
print(res)