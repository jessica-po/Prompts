n = int(input())
nim = []
for i in range(n):
  a,k = map(int,input().split())
  while a%k != 0 and a>k:
    t = a//k
    if t+1>=a%k:
      a -= t+1
    else:
      y = a%k
      a -= y//(t+1)*(t+1)
  if a<k:
    x = 0
  elif a%k == 0:
    x = a//k
  nim.append(x)
ans = 0
for i in nim:
  ans ^= i
if ans == 0:
  print("Aoki")
else:
  print("Takahashi")