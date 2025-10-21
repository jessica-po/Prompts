n, x = map(int, input().split())
a = [int(x) for x in input().split()]
def solve(a, s):
  #print (a)
  a.append((-1, 0))
  a.sort()
  b = []
  for i in range(1, len(a)):
    if a[i][0] != a[i-1][0]:
      b.append(a[i])
    else:
      b[-1] = (a[i][0], b[-1][1] + a[i][1])
  for i in range(len(b)):
    t = b[i][1]
    cnt = 0
    while t%x == 0:
      t //= x
      cnt += 1
    b[i] = (b[i][0] + cnt, t)
  #print (b)
  z = min(min(b)[0], s)
  if z == 0:
    return 0
  return z + solve([(x[0]-z, x[1]) for x in b], s-z)
s = sum(a)
print(pow(x, solve([(s-x, 1) for x in a], s), 10**9+7))