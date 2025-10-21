from sys import stdin
from fractions import gcd
lines = list([_f for _f in stdin.read().split('\n') if _f])

def parseline(line):
	return list(map(int, line.split()))

lines = list(map(parseline, lines))

l, r = lines[0]

for a in range(l, r+1):
	for b in range(a, r+1):
		for c in range(b, r + 1):
			if gcd(a, b) == gcd(b, c) == 1 != gcd(a, c):
				print(a, b, c)
				return
print(-1)