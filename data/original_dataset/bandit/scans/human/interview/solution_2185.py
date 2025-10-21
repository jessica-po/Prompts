import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
read = lambda : list(map(int, input().split()))
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}{}".format(i, sep))
INF = float('inf')
MOD = int(1e9 + 7)

for _ in range(int(input())):
  n = int(input())
  a = list(read())
  b = list(read())

  arr = []
  for i in range(n):
    if a[i] != b[i]:
      arr.append((i, b[i] - a[i]))

  
  flag = True 
  s = []
  for i, j in arr:
    if j <= 0:
      flag = False
      break 
    s.append(j)
  
  for i in range(1, len(arr)):
    if arr[i][0] != arr[i-1][0] + 1:
      flag = False 
      break 
  
  if len(set(s)) >= 2:
    flag = False 

  if flag:
    print("YES")
  else:
    print("NO")