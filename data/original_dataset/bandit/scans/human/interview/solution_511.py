from fractions import gcd
x, y = map(int, input().split())

a = int(x**.5 + 1)
p = []
x1 = x
for i in range(2, a + 1):
  if (x1 % i == 0):
    p.append(i)
    while (x1 % i == 0):
      x1 //= i
if (x1 > 1):
  p.append(x1)
ans = 0
while (y != 0):
  r = gcd(x, y)
  x //= r
  y //= r
  max_can = 0
  for i in range(len(p)):
    if (x % p[i] == 0):
      max_can = max(max_can, y - y % p[i])
  ans += y - max_can
  y = max_can
print(ans)