t, s, x = list(map(int, input().split()))
f = False
if x - 1 > t and (x - 1 - t) % s == 0:
    f = True
if x >= t and (x - t) % s == 0:
    f = True
if f:
    print('YES')
else:
    print('NO')