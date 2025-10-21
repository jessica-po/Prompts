import sys
import time

for line in sys.stdin:
    ll = len(line) - 1
    fail = 0
    for i in range(ll):
        if i == ll - 1 - i:
            if int(line[i]) not in [3, 7]:
                fail = 1
            continue
        x = int(line[i])
        y = int(line[ll - 1 - i])
        if (x, y) not in [(3, 3), (4, 6), (6, 4), (7, 7), (8, 0), (0, 8), (5, 9), (9, 5)]:
            fail = 1
    if fail:
        print("No")
    if not fail:
        print("Yes")