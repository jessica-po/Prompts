h, n = list(map(int, input().split()))
c, m = 0, 2 ** h
r = 0
while m > 1:
    if c == 0:
        if n > m // 2:
            r += m - 1
            n -= m // 2
            c = 1 - c
    else:
        if n > m // 2:
            n -= m // 2
        else:
            r += m - 1
            c = 1 - c
    c = 1 - c
    r += 1
    m //= 2
    #print(c, m, r, n)
print(r)