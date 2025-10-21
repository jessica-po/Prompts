n = int(input())
a = sorted([list(map(int, input().split())) for i in range(n)])

import itertools
for x in range(1,10**n):
  good = False
  s = str(x)
  for p in itertools.permutations(a, len(s)):
    good |= all([int(s[i]) in v for i, v in enumerate(p)])
  if not good:
    print(x-1)
    return
    
print((10**n)-1)