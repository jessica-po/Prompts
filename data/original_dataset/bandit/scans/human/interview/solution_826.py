import sys

# B - log
import math

n = int(input())
i = math.floor(math.sqrt(n*2))-1

while True:
  total = (2+i) * (i+1) // 2

  if total <= n+1:
    i += 1
  else:
    break

print(n-i+1)