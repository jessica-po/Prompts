n = 100001
p = [0] * n
t = [[] for i in range(n)]
t[1] = [1]
for i in range(2, n):
    if not t[i]:
        t[i] = [i]
        for j in range(2 * i, n, i): t[j].append(i)
input()
a = list(map(int, input().split()))
for i in a:
    x = max(p[j] for j in t[i]) + 1
    for j in t[i]: p[j] = x
print(max(p))