#!/bin/python3

a = input()

a = a + a

ma = 1
last = 'x'
pos = 0
cur = 0
while pos < len(a):
	if a[pos] != last:
		cur += 1
		ma = max(ma, cur)
	else:
		cur = 1
	last = a[pos]
	pos += 1

print(min(ma, len(a) // 2))