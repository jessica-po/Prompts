from operator import neg
n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]

def check(max_h):
    k = n // 2
    b = []
    for w, h in a:
        if h > max_h:
            if k <= 0 or w > max_h:
                return 1 << 60
            b.append((h, w))
            k -= 1
        else:
            b.append((w, h))
    b.sort(key=lambda t: t[1] - t[0])
    r = 0
    for w, h in b:
        if k > 0 and w <= max_h and h < w:
            r += h
            k -= 1
        else:
            r += w
    return r * max_h

print(min(check(h) for h in range(1, 1001)))