n, k = map(int, input().split())
t = list(map(int, input().split()))
t = [t[0]] + [t[i] for i in range(1, len(t)) if t[i] != t[i - 1]]
p = [0] * (k + 1)
for i in range(1, len(t) - 1):
    if t[i - 1] == t[i + 1]: p[t[i]] += 2
    else: p[t[i]] += 1
p[t[0]] += 1
p[t[-1]] += 1
print(p.index(max(p)))