import itertools
import operator


n, x = list(map(int, str.split(input())))
a = []
b = []
for _ in range(n):

    t, h, m = list(map(int, str.split(input())))
    (a if t else b).append((h, m))

best = 0
for ca, cb in ((a, b), (b, a)):

    cx = x
    count = 0
    ca, cb = ca[:], cb[:]
    while True:

        available = tuple([candy for candy in enumerate(ca) if candy[1][0] <= cx])
        if available:

            i, candy = max(available, key=lambda candy: candy[1][1])
            ca.pop(i)
            count += 1
            cx += candy[1]

        else:

            break

        ca, cb = cb, ca

    best = max(best, count)

print(best)