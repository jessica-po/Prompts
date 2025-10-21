n, m = map(int, input().split())
if (m >= n): print(n)
else:
    c = n - m
    l = 0
    r = 10 ** 18
    while r - l > 1:
        md = (r + l) // 2
        if (1 + md) * md // 2 < c:
            l = md
        else:
            r = md
    print(r + m)