import time
import random

l = list(map(int, input().split()))
assert len(l) == l[0] + 1
l = l[1:]
l.sort()

v = [0 for i in range(10 ** 4)]
for i in range(4 * 10**5):
    v[random.randrange(0, len(v))] = random.randrange(-1000, 1000)

print(' '.join(map(str, l)))