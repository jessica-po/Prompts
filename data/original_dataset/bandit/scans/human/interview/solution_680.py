ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))


def f(cx, ax, bx, cy, ay, by):
    mxy = max(ay, by, cy)
    mny = min(ay, by, cy)
    print(abs(cx - bx) + mxy - mny + 1)
    for i in range(mny, mxy + 1):
        print(ax, i)
    if cx <= bx:
        for i in range(cx, ax):
            print(i, cy)
        for i in range(ax + 1, bx + 1):
            print(i, by)
    else:
        for i in range(bx, ax):
            print(i, by)
        for i in range(ax + 1, cx + 1):
            print(i, cy)


if cx <= ax <= bx or bx <= ax <= cx:
    f(cx, ax, bx, cy, ay, by)
elif cx <= bx <= ax or ax <= bx <= cx:
    f(cx, bx, ax, cy, by, ay)
elif bx <= cx <= ax or ax <= cx <= bx:
    f(bx, cx, ax, by, cy, ay)