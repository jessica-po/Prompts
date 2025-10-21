from sys import *
f = list(map(int, stdin.read().split()))

n, m = f[0], f[1]
d = [[] for i in range(100001)]

for j in range(2, len(f), 3):
    x, y, w = f[j:j + 3]
    d[w].append((y, x))

s = [0] * (n + 1)
for q in d:
    for y, k in [(y, s[x]) for y, x in q]: s[y] = max(s[y], k + 1)
print(max(s))