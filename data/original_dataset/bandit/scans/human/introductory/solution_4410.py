import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br

def solve():
  n, k = I()
  s = input()
  ans = 0
  last = -INF
  for i in range(n):
    if s[i] == '1':
      if i - last <= k:
        ans -= 1
      last = i
      count = 0
      continue
    if i - last > k:
      ans += 1
      last = i 

  print(ans)

t, = I()
while t:
  t -= 1
  solve()