n = int(input())

a = list(map(int, input().split()))
aord = sorted([i for i in range(n)], key=lambda x: a[x] * (n - x) * (x + 1))

b = sorted(map(int, input().split()))[::-1]
new_b = [0] * n
for i in range(n):
    new_b[aord[i]] = b[i]
b = new_b

m = 998244353

c = [0] * n
for i in range(n):
    c[i] = a[i] * b[i] % m

ans = 0
for i in range(n):
    u = c[i] * (n - i) * (i + 1) % m
    ans = (ans + u) % m
print(ans)