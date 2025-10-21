from math import sqrt
from collections import Counter


def f(h, w, y, x):
    return h * w * (h + w - (x + y + 1) * 2) // 2 + h * x * (x + 1) + w * y * (y + 1)


def check(h, w, y, x, cnt):
    for i in range(1, y + 1):
        for j in range(i + 1, i + x + 1):
            cnt[j] -= 1
        for j in range(i, i + w - x):
            cnt[j] -= 1
    for i in range(h - y):
        for j in range(i + 1, i + x + 1):
            cnt[j] -= 1
        for j in range(i, i + w - x):
            cnt[j] -= 1
    if any(cnt.values()):
        return
    print(f'{h} {w}\n{y+1} {int(x)+1}')
    raise TabError


def getyx(h, w, tot, cnt):
    b = (w - 1) * .5
    c = h * (tot - h * (w * w - 2 * w * (1 - h) - 1) * .25)
    for y in range((h + 3) // 2):
        d = (c - h * y * (w * y - h * w + w))
        if d >= 0:
            x = b - sqrt(d) / h
            if x.is_integer() and x >= 0.:
                check(h, w, y, int(x), cnt.copy())


def main():
    n, l = int(input()), list(map(int, input().split()))
    cnt, r, R, tot = Counter(l), 1, max(l), sum(l)
    for r in range(1, R + 1):
        if cnt[r] < r * 4:
            break
    try:
        for h in range(r * 2 - 1, int(sqrt(n)) + 1):
            if not n % h:
                w = n // h
                if f(h, w, h // 2, w // 2) <= tot <= f(h, w, 0, 0):
                    getyx(h, w, tot, cnt)
    except TabError:
        return
    print(-1)


def __starting_point():
    main()

__starting_point()