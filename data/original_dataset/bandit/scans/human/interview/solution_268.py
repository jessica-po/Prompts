#!/usr/bin/env python3

from bisect import bisect

[n, k, d] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))
if k == 1:
	print ('YES')
	return

ais.sort()

# can do ais[i:]
cando = [False for _ in range(n)]
j = n - 1  # j is such that a[j] > a[i] + d >= a[j - 1]  (upper_bound) a[:j] <= a[i] + d < a[j:]
count = 0  # sum(cando[i + k:j + 1])
for i in reversed(list(range(n))):
	if i + k < n and cando[i + k]:
		count += 1
	if n - i < k:
		continue
	if ais[-1] - ais[i] <= d:
		cando[i] = True
		continue
	while ais[j - 1] > ais[i] + d:
		if cando[j]:
			count -= 1
		j -= 1
	cando[i] = (count > 0)
	

if cando[0]:
	print ('YES')
else:
	print ('NO')