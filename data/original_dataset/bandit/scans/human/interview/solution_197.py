from bisect import bisect_left

M = 998244353

def pw(x, y):
    if y == 0:
        return 1
    res = pw(x, y//2)
    res = res * res % M
    if y % 2 == 1:
        res = res * x % M
    return res

def cal(x, y):
    y += x - 1
    res = 1
    for i in range(1, x + 1):
        res = res * (y - i + 1)
        res = res * pw(i, M - 2) % M
    return res % M

n = int(input())
a = []
b = []
res = 1
for i in range(n):
    a.append(list(map(int, input().split())))
    res = res * (a[-1][1] + 1 - a[-1][0]) % M
    b.append(a[-1][0])
    b.append(a[-1][1] + 1)
    b = set(b)
    b = sorted(list(b))

g = [b[i + 1] - b[i] for i in range(len(b) - 1)]

for i in range(n):
    a[i][0] = bisect_left(b, a[i][0])
    a[i][1] = bisect_left(b, a[i][1] + 1)

a = a[::-1]

f = [[0 for _ in range(len(b))] for __ in range(n)]

for i in range(a[0][0], len(b)):
    if i == 0:
        f[0][i] = g[i]
    else:
        if i < a[0][1]:
            f[0][i] = (f[0][i - 1] + g[i]) % M
        else:
            f[0][i] = f[0][i - 1]
        
for i in range(1, n):
    for j in range(a[i][0], len(b)):
        if j > 0:
            f[i][j] = f[i][j - 1]
        if j < a[i][1]:
            for k in range(i, -1, -1):
                if a[k][1] <= j or j < a[k][0]:
                    break
                if k == 0 or j != 0:
                    tmp = cal(i - k + 1, g[j])
                    if k > 0:
                        f[i][j] += f[k - 1][j - 1] * tmp % M
                    else:
                        f[i][j] += tmp
                    f[i][j] %= M
                    
#print(f)
#print(f[n - 1][len(b) - 1], res)
print(f[n - 1][len(b) - 1] * pw(res, M - 2) % M)