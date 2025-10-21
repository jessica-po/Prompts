# import sys
# sys.stdin = open('cf614b.in', 'r')

import re

p = re.compile(r'^10*$')

n = int(input())
a = input().split()

extra = '1'
numzero = 0

for ai in a:
	if ai == '0':
		print(0)
		return
	elif p.match(ai):
		numzero += len(ai) - 1
	else:
		extra = ai

print(extra + '0' * numzero)