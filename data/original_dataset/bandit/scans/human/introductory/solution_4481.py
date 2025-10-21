from collections import Counter
n = int(input())
ss = [input() for _ in range(n)]
ss.sort()
c = Counter()
mc = 0
for s in ss:
  c[s] += 1
  mc = max(mc, c[s])
seen = set()
for s in ss:
  if c[s] == mc and s not in seen:
    print(s)
    seen.add(s)