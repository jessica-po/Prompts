n = int(input())
a = list(map(int, input().split()))

b = sorted(a[::])
for i in range(n):
    if b[i] == b[i+1]:
        d = b[i]

l, r = -1, -1
for i in range(n+1):
    if l < 0:
        if a[i] == d:
            l = i
    else:
        if a[i] == d:
            r = i

f = [1 for _ in range(n+2)]
f_inv = [1 for _ in range(n+2)]
mod = 10 ** 9 + 7
for i in range(1, n+2):
    f[i] = f[i-1] * i % mod
    f_inv[i] = pow(f[i], mod-2, mod)

def comb(n, k):
    return f[n] * f_inv[k] * f_inv[n-k] % mod


for k in range(1, n+2):
    ans = 0

    if k >= 2:
        ans += comb(n-1, k-2)
        ans %= mod

    if n - 1 >= k:
        ans += comb(n-1, k)
        ans %= mod

    if n >= k:
        ans += 2 * comb(n-1, k-1)
        ans %= mod

    if n + l - r >= k - 1:
        ans -= comb(n+l-r, k-1)
        ans %= mod

    print(ans)