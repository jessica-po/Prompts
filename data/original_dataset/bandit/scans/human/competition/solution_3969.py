n, m = map(int, input().split())
t = [int(input().split()[0]) for i in range(n)]
p = [0] * (m + 1)
for i, j in enumerate(t): p[j] = min(p[j], min(p[: j])) - 1
print(n + min(p))