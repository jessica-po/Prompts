from sys import *
from collections import *
from math import *

input = stdin.readline

tc = int(input())
for tcase in range(tc):
	n, k = map(int, input().split())
	lo = 1
	hi = 10 ** 19
	ans = -1
	while (lo <= hi):
		mid = (lo + hi) // 2
		divi = mid - mid // n
		if (divi >= k):
			ans = mid
			hi = mid - 1
		else:
			lo = mid + 1
	print(ans)