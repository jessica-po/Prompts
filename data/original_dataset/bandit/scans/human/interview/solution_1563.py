n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))
t = {i: set() for i in set(c[1:])}
for i in range(m):
    a, b = map(int, input().split())
    if c[a] != c[b]:
        t[c[a]].add(c[b])
        t[c[b]].add(c[a])
j, k = c[1], 0
for i, s in t.items():
    l = len(s)
    if l >= k: 
        if l > k: j, k = i, l
        elif j > i: j = i
print(j)