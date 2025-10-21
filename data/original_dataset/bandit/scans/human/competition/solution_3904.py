__, s = input(), input()
a, n = 0, 0
pt = {'(': 1, ')': -1}
for c in s:
  da = pt.get(c, 0)
  if a < 0 or a + da < 0:
    n += 1
  a += da
if a != 0:
  print(-1)
else:
  print(n)