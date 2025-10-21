import sys
import math

Q = 998244353
n, m = list(map(int, sys.stdin.readline().strip().split()))

z = [1, 1]
f = [1, 1]
for i in range (0, n):
    f[0] = f[0] * (n - i) % Q
    f[1] = f[1] * (n + m - i) % Q
    z = [(z[0]*f[1]+z[1]*f[0]) % Q, (z[1]*f[1]) % Q]
ans = [z[0] * (m+1), z[1]]
for i in range (2, n + 1):
    ans = [(ans[0] * i * z[1] + ans[1] * m * z[0]) % Q, (ans[1] * i * z[1]) % Q]
y = ans[1]
ans = ans[0]
q = Q - 2
while q > 0:
    if q % 2 == 1:
        ans = (ans * y) % Q
    q = q // 2
    y = (y * y) % Q
print(ans)