from collections import Counter
from itertools import product
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1 = [0]
b1 = [0]
for i in range(n):
  if a[i] == 1:
    a1[-1] += 1
  elif a1[-1] != 0:
    a1.append(0)
for i in range(m):
  if b[i] == 1:
    b1[-1] += 1
  elif b1[-1] != 0:
    b1.append(0)
pr = []
for i in range(1,int(k**0.5)+1):
  if k%i == 0 and k//i <= 40000:
    pr.append((i,k//i))
    if i != k//i:
      pr.append((k//i,i))
ca = Counter(a1)
cb = Counter(b1)
ans = 0
for i,j in product(ca.items(),cb.items()):
  for x,y in pr:
    if i[0] >= x and j[0] >= y:
      ans += i[1]*j[1]*(i[0]-x+1)*(j[0]-y+1)
print(ans)