from math import *
n, m = list(map(int, input().split()))
if m < n - 1:
    print('Impossible')
    return
r = [(i + 1, i + 2) for i in range(n - 1)]
k = n - 1
if k >= m:
    print('Possible')
    for x in r:
        print(*x)
    return
for i in range(1, n + 1):
    for j in range(i + 2, n + 1):
        if gcd(i, j) == 1:
            r.append((i, j))
            k += 1
        if k >= m:
            print('Possible')
            for x in r:
                print(*x)
            return
print('Impossible')