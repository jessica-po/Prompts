n = int(input())
a = [int(x) for x in input().split()]
a.sort()
mod = 10 ** 9 + 7

def p(p):
  ans = 1
  for i in range(p):
    ans *= 2
    ans %= mod
  return ans

if n % 2 == 1:
  res = True
  for i in range(n):
    if a[i] != ((i + 1) // 2) * 2:
      res = False
  if res:
    print(p(n // 2))
  else:
    print(0)
    
else:
  res = True
  for i in range(n):
    if a[i] != (i // 2) * 2 + 1:
      res = False
  if res:
    print(p(n // 2))
  else:
    print(0)