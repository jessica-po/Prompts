import numpy as np

k, q = map(int, input().split())
d = np.array(list(map(int, input().split())))

for i in range(q):
  n, x, m = map(int, input().split())
  mod_d = d % m
  modsum_d = mod_d.cumsum()
  _q, _m = divmod(n - 1, k)
  
  ans = modsum_d[k - 1] * _q
  if _m > 0:
    ans += modsum_d[_m - 1]
  ans = n - 1 - (ans + x % m) // m - np.count_nonzero(mod_d == 0) * _q
  if _m > 0:
    ans -= np.count_nonzero(mod_d[0 : _m] == 0)
  print(ans)