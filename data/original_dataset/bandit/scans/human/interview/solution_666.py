def f(m):
    return m * (m + 1) // 2

n = int(input())
l, r = 0, n
while r - l > 1:
    m = (r + l) // 2
    if f(m) >= n:
        r = m
    else:
        l = m
n -= f(l)
print(n)