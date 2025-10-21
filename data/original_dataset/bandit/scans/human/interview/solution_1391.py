3

def readln(): return tuple(map(int, input().split()))

n, m, a = readln()
b = list(sorted(readln()))
p = list(sorted(readln()))

l = ost = 0
r = min(m, n) + 1

while r - l > 1:
    k = (r + l) // 2
    s = d = 0
    for x, y in zip(b[-k:], p[:k]):
        if x < y:
            d += y - x
        s += y
    if d <= a:
        l = k
        ost = max(0, s - a)
    else:
        r = k

print(l, ost)