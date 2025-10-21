ans = 0
mod = 1000000007
a, b, n = list(map(int, input().split()))
s = set()
for x in range(2, 1 << 8):
    z = 0
    while x > 1:
        z = z * 10 + (a, b)[x & 1]
        x >>= 1
    s.add(z)
f = [1] * (n + 1)
for i in range(1, n + 1):
    f[i] = f[i - 1] * i % mod
for x in range(n + 1):
    if x * a + (n - x) * b in s:
        ans += pow(f[x] * f[n - x], mod - 2, mod)
        ans %= mod
print(ans * f[n] % mod)