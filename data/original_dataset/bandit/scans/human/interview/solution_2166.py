input()
t = list(map(int, input().split()))
s, m = 0, 1000000007
p = {i for i, q in enumerate(t, 1) if q == -1}
n, k = len(p), len(p - set(t))
d, c = 2 * (n & 1) - 1, 1
for j in range(n + 1):
    d = -d * max(1, j) % m
    if n - j <= k:
        s += c * d
        c = c * max(1, n - j) * pow(k - n + j + 1, m - 2, m) % m
print(s % m)