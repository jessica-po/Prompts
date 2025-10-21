from math import gcd

N = int(input())
num_lis = list(map(int, input().split()))
c = True

def osa_k(max_num):
  lis = [i for i in range(max_num+1)]
  p = 2
  while p**2 <= max_num:
    if lis[p] == p:
      for q in range(2*p, max_num+1, p):
        if lis[q] == q:
          lis[q] = p
    p += 1
  return lis

hoge = 0
for i in num_lis:
  hoge = gcd(hoge, i)
if hoge > 1:
  print("not coprime")
  return

d_lis = osa_k(10**6+10)
tmp = set()
for i in num_lis:
  num = i
  new_tmp = set()
  while num > 1:
    d = d_lis[num]
    new_tmp.add(d)
    num //= d
  for j in new_tmp:
    if j in tmp:
      c = False
      break
    else:
      tmp.add(j)
  else:
    continue
  break

if c:
  print("pairwise coprime")
else:
  print("setwise coprime")