import sys

class Fenwick(object):
  def __init__(self, n):
    self.n = n
    self.a = [10**9 for i in range(n)]
    self.w= 10**9

  def zag(self, i, zn):
    self.w= min(self.w, zn)
    while i < self.n:
      self.a[i] = min(self.a[i], zn)
      i = (i | (i + 1))

  def pol(self, r):
    ans= 10**9
    while r >= 0:
      if ans> self.a[r]:
        ans= self.a[r]
      if ans== self.w:
        break
      r = (r & (r + 1)) - 1
    return ans

n, m = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]

nd= [-1 for i in range(0, len(a))]
vi= {}
for i in range(0, len(a)):
  if a[i] in vi:
    nd[i] = vi[a[i]]
  vi[a[i]] = i

inp= sys.stdin.readlines()
och= [[] for i in range(n)]
for i in range(m):
  l, r = inp[i].split()
  och[int(r) - 1].append((int(l) - 1, i))

der = Fenwick(2 ** 19)
ans= [None for i in range(0, m)]
le= -1
for r in range(n):
  if nd[r] != -1:
    der.zag(500000 - nd[r] + 1, r - nd[r])
    le = max(le, nd[r])
  for (l, ind) in och[r]:
    if l > le:
      ans[ind] = -1
      continue
    zn= der.pol(500000 - l + 1)
    if zn== 10**9:
      zn= -1
    ans[ind] = zn

print('\n'.join(str(zn) for zn in ans))