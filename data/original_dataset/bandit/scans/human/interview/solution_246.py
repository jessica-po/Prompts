def check(x, s):
    k = 0
    for i in str(x):
        k += int(i)
    return x - k >= s


n, s = map(int, input().split())
l = 0
r = n
while r - l > 1:
    m = (l + r) // 2
    if check(m, s):
        r = m
    else:
        l = m
if check(r, s):
    print(n - r + 1)
else:
    print(0)