from sys import *
from math import *

mod = 1000000000
f = [0 for i in range(200)]
f[0] = f[1] = 1
for i in range(2, 200):
  f[i] = f[i - 1] + f[i - 2]
n, m = stdin.readline().split()
n = int(n)
m = int(m)
a = list(map(int, stdin.readline().split()))
for i in range(m):
  tp, x, y = stdin.readline().split()
  tp = int(tp)
  x = int(x)
  y = int(y)
  if tp == 1:
    x -= 1
    a[x] = y
  else:
    s = 0
    x -= 1
    y -= 1
    for p in range(y - x + 1):
      s += f[p] * a[x + p]
    print(s % mod)