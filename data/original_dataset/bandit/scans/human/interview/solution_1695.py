from collections import Counter
n, m = map(int, input().split())
l = [input() for _ in range(n)]
v = [*map(int, input().split())]
res = 0
for i in range(m):
    res += v[i] * max(Counter(s[i] for s in l).values())
print(res)