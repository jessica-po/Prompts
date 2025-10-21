import sys
fin = sys.stdin

n, k = map(int, fin.readline().split())
c = list(map(int, fin.readline().split()))
s = [0] * (n + 1)
for i in range(n):
  s[i + 1] = s[i] + c[i]

ms = [i for i in range(n)]
for i in range(n - k - 1, k - 1, -1):
  s_last = s[ms[i + 1] + k] - s[ms[i + 1]]
  s_curr = s[i + k] - s[i]
  if s_curr >= s_last:
    ms[i] = i
  else:
    ms[i] = ms[i + 1]

a, b = 0, k

for i in range(n - 2 * k + 1):
  j = i + k
  sa = s[j] - s[i]
  sb = s[ms[j] + k] - s[ms[j]]
  if sa + sb > s[a + k] - s[a] + s[b + k] - s[b]:
    a, b = i, ms[j]

print(a + 1, b + 1)