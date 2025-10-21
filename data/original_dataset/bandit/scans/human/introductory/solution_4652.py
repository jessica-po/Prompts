'''input
5
4
1 2 3 4
3
1 3 2
5
1 2 3 5 4
1
1
5
3 2 1 5 4

'''
import sys
from collections import defaultdict as dd
from itertools import  permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
from  heapq import heappush as hpush
from heapq import heappop as hpop
mod=10**9+7

def ri(flag=0):
	if flag==0:
		return [int(i) for i in sys.stdin.readline().split()]
	else:
		return int(sys.stdin.readline())



for _ in range(ri(1)):
	n = ri(1)
	a= ri()
	idx = a.index(1)

	check1 = 1
	check2 =1
	for i in range(n):
		if a[(idx+i)%n] == i+1:
			pass
		else:
			check1=0
	a=a[::-1]
	idx = a.index(1)
	for i in range(n):
		if a[(idx+i)%n] == i+1:
			pass
		else:
			check2=0

	if check1==1 or check2==1:
		print("YES")
	else:
		print("NO")