n, t = map(int, input().split())
s = bin(n + 2)[2:]
l = len(s)

if t & (t - 1):
    ans = 0
else:
    t = t.bit_length()
    f = [[0] * (l + 1) for i in range(l + 1)]
    for i in range(l + 1):
        f[i][0] = f[i][i] = 1
        for j in range(1, i):
            f[i][j] = f[i - 1][j - 1] + f[i - 1][j]

    ans = c = 0
    for i in range(l):
        if s[i] == '1':
            if t - c <= l - i - 1:
                ans += f[l - i - 1][t - c]
            c += 1
    if t == 1: ans -= 1
print(ans)