def f(a, ind):
    if a[ind] == 0:
        return -1
    k = a[ind] // 14
    x = a[ind] % 14
    b = a[:]
    b[ind] = 0
    for j in range(14):
        b[j] += k
    for j in range(ind + 1, ind + x + 1):
        j1 = j % 14
        b[j1] += 1
    res = 0
    for j in range(14):
        if b[j] % 2 == 0:
            res += b[j]
    return res
a = list(map(int, input().split()))
ans = 0
for i in range(14):
    cur = f(a, i)
    ans = max(ans, cur)
print(ans)