def seg(x, y, h):
    A = [x - h, x + h]
    B = [y - h, y + h]
    Z = []
    for a in A:
        for b in B:
            Z.append(a * b)
    Z.sort()
    return (Z[0], Z[-1])

def check(a, b, c, d, h):
    x1, y1 = seg(a, d, h)
    x2, y2 = seg(b, c, h)
    return max(x1, x2) <= min(y1, y2)

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
l = 0
r = max(abs(a), abs(b), abs(c), abs(d))
for i in range(100):
    m = (l + r) / 2
    if check(a, b, c, d, m):
        r = m
    else:
        l = m
print((r + l) / 2)