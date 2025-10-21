from math import ceil

def mkgr(n, srs, k):
  res = [str(n-1)]
  for d in srs[1]:
    res.append("%i %i" % (srs[0][0]+1, d+1))
  for i in range(2, len(srs)):
    h, hs= 0, 0
    for j in range(len(srs[i])):
      res.append("%i %i" % (srs[i][j]+1, srs[i-1][h]+1))
      hs += 1
      if hs == k-1:
        h += 1
        hs = 0
      
  return res

def test(n,k,dists):
  m = max(dists)
  srs = [[] for i in range(m+1)]
  for i in range(n):
    srs[dists[i]].append(i)
  if [] in srs:
    return ["-1"]
  if len(srs[0]) != 1:
    return ["-1"]
  if len(srs[1]) > k:
    return ["-1"]
  for i in range(1, m):
    if ceil(len(srs[i+1])/len(srs[i])) + 1 > k:
      return ["-1"]
  return mkgr(n, srs, k)

n, k = list(map(int, input().split()))
dists = list(map(int, input().split()))
res = test(n,k,dists)
print("\n".join(res))