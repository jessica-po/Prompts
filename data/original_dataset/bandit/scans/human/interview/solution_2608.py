def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

def pre(x, y):
    w = x * (y // 2) + (y % 2) * (x + 1) // 2
    b = x * (y // 2) + (y % 2) * x // 2
    assert w + b == x * y
    return w

def count(x1, y1, x2, y2):
    w = pre(x2, y2) + pre(x1 - 1, y1 - 1) - pre(x2, y1 - 1) - pre(x1 - 1, y2)
    b = (x2 - x1 + 1) * (y2 - y1 + 1) - w
    return w, b

for t in range(ii()):
    n, m = mi()
    x1, y1, x2, y2 = mi()
    x3, y3, x4, y4 = mi()
    w = pre(m, n)
    b = m * n - w
    # white spill
    wc, bc = count(x1, y1, x2, y2)
    w -= wc
    b -= bc
    w += (x2 - x1 + 1) * (y2 - y1 + 1)
    # black spill
    if max(x1, x3) <= min(x2, x4) and max(y1, y3) <= min(y2, y4):
        x5 = max(x1, x3)
        y5 = max(y1, y3)
        x6 = min(x2, x4)
        y6 = min(y2, y4)
        w -= (x6 - x5 + 1) * (y6 - y5 + 1)
        wc, bc = count(x5, y5, x6, y6)
        w += wc
        b += bc
    wc, bc = count(x3, y3, x4, y4)
    w -= wc
    b -= bc
    b += (x4 - x3 + 1) * (y4 - y3 + 1)
    print(w, b)