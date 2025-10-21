import copy
import fractions
import itertools
import numbers
import string
import sys

###

def to_basex(num, x):
	while num > 0:
		yield num % x
		num //= x

def from_basex(it, x):
	ret = 0
	p = 1
	for d in it:
		ret += d*p
		p *= x
	return ret

###

def core():
	n = int(input())
	a = [int(x) for x in input().split()]
	
	m = min(a)
	s = sum(a)
	ans = s
	for ai in a:
		for d in range(1, ai+1):
			if ai % d == 0:
				cand = s - ai - m + ai//d + m*d
				ans = min(ans, cand)
	
	print(ans)


core()