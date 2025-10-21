from itertools import accumulate
from bisect import bisect_right
import sys

n, q = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
k = list(map(int, sys.stdin.readline().split()))

s = list(accumulate(a))

sofar = 0
for x in k:
    sofar += x
    if sofar >= s[-1]:
        sofar = 0
    sys.stdout.write(str(n - bisect_right(s, sofar)) + '\n')