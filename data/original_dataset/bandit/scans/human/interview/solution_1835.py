import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
read = lambda : list(map(int, input().split()))
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}".format(i) + sep)
INF = float('inf')
MOD = int(1e9 + 7)

for _ in range(int(input())):
  n = int(input())
  arr = sorted([input() for i in range(n)], key=lambda x:len(x))

  zero_cnt, one_cnt = 0, 0
  for i in arr:
    zero_cnt += i.count('0')
    one_cnt += i.count('1')
  total = (zero_cnt//2) + (one_cnt//2)
  
  ans = 0

  for i in arr:
    if total >= len(i)//2:
      total -= len(i)//2 
      ans += 1
  
  print(ans)