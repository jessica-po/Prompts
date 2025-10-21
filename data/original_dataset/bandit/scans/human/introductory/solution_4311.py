from collections import defaultdict

d = defaultdict(bool)

n = int(input())
for i in range(1000000):

    if d[n]:
        print((i + 1))
        return
    d[n] = True
    if n & 1:
        n = n * 3 + 1
    else:
        n >>= 1