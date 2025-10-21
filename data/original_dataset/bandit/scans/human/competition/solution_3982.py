MOD = 10 ** 9 + 7
BAD = ([0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1])

def zfunc(s):
    z = [0] * len(s)
    l = r = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

n = int(input())
s = []
sm = 0
for i in range(1, n + 1):
    s.append(int(input()))
    cur = 0
    f = [0] * (i + 1)
    sum4 = f[i] = 1
    for j in range(i - 1, -1, -1):
        if j + 4 < i:
            sum4 -= f[j + 5]
        if j + 4 <= i and s[j : j + 4] in BAD:
            f[j] -= f[j + 4]
        f[j] = (f[j] + sum4) % MOD
        sum4 += f[j]
    z = zfunc(s[::-1])
    new = i - max(z)
    sm = (sm + sum(f[:new])) % MOD
    print(sm)