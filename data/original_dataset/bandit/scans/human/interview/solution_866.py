from functools import reduce

x,y=list(map(int,input().split()))
mod = 10 ** 9 + 7

if (2 * y - x) % 3 != 0 or (2 * x - y) % 3 != 0:
  print("0")
  return
  
a,b = (2 * y - x) // 3, (2 * x - y) // 3 

r = min(a,b)

if r == 0:
  print("1")
elif r < 0:
  print("0")
else:
  numerator = reduce(lambda x, y: x * y % mod, range(a + b - r + 1, a + b + 1))
  denominator = reduce(lambda x, y: x * y % mod, range(1,r + 1))
  print(numerator * pow(denominator, mod - 2, mod) % mod)