n, m = [int(x) for x in input().split()]
a = [[int(c == '.') for c in input()] for i in range(n)]

def rotate(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][n - 1 - i] = a[i][j]
    return b

def calc(a):
    n = len(a)
    m = len(a[0])
    alive = a[0][:]
    alive[0], alive[m - 1] = 0, 0
    ans_l, ans_r, ans_u = 0, 0, 0
    ans_bs = [0] * m
    for i in range(1, n - 1):
        s = 0
        for j in range(1, m - 1):
            if a[i][j]:
                if alive[j]:
                    ans_u += s - alive[j - 1]
                ans_bs[j] += s
                s += alive[j]
            else:
                s = 0
                ans_bs[j] = 0
                alive[j] = 0
        if a[i][m - 1]:
            ans_r += s
        s = 0
        for j in range(m - 2, 0, -1):
            if a[i][j]:
                if alive[j]:
                    ans_u += s - alive[j + 1]
                ans_bs[j] += s
                s += alive[j]
            else:
                s = 0
                ans_bs[j] = 0
                alive[j] = 0
        if a[i][0]:
            ans_l += s
    ans_u //= 2
    ans_b = sum(a[n - 1][i] * (ans_bs[i] + alive[i]) for i in range(1, m - 1))
    return ans_l, ans_r, ans_u, ans_b
ans = 0
ans_l, ans_r, ans_u, ans_b = calc(a)
ans += ans_l + ans_r + ans_u + ans_b
a = rotate(a)
ans_l, _, ans_u, ans_b = calc(a)
ans += ans_l + ans_u + ans_b
a = rotate(a)
ans_l, _, ans_u, _= calc(a)
ans += ans_l + ans_u
a = rotate(a)
_, _, ans_u, _= calc(a)
ans += ans_u
print(ans)