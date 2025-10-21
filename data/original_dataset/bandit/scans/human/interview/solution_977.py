import sys
from bisect import bisect_right as br
input = sys.stdin.readline
n, p = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
table = [0] * (10 ** 5 + 1)
for x in range(10 ** 5 + 1):
  r = br(a, x)
  table[x] = r
res = []
#print(table[: 100])
for x in range(1, 2001):
  t = 1
  q = x + 0
  for i in range(n):
    t *= max(0, table[q] - i)
    t %= p
    q += 1
  if t % p: res.append(x)
print(len(res))
print(*res)