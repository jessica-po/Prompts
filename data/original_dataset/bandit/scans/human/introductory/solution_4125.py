from fractions import gcd
from functools import reduce

n, x = list(map(int, input().split()))
c = list(map(int, input().split()))

print((reduce(gcd, [abs(i-x) for i in c])))