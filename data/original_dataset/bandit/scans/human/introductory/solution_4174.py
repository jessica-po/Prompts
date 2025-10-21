import itertools
import bisect

n, x = map(int, input().split())
l = list(map(int, input().split()))

a = list(itertools.accumulate(l, initial=0))
print(bisect.bisect_right(a, x))