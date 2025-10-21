import sys
from collections import defaultdict
from copy import copy

R = lambda t = int: t(input())
RL = lambda t = int: [t(x) for x in input().split()]
RLL = lambda n, t = int: [RL(t) for _ in range(n)]

def solve():
  n, x = RL()
  A = RL()
  A.sort(reverse = True)
  s = c = m = 0
  for a in A:
    s += a
    c += 1
    if s >= x * c:
      m = c    
  print(m)
      
T = R()
for _ in range(T):
  solve()