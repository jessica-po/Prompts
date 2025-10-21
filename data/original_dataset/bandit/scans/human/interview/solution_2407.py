import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
read = lambda : map(int, input().split())
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}".format(i) + sep)
INF = float('inf')
MOD = int(1e9 + 7)

for q in range(int(input())):
  n, r = read()
  arr = sorted(set(read()), reverse=True)
  s = 0
  ans = 0

  for i in arr:
    if s >= i:
      break

    s += r
    ans += 1

  write(ans)