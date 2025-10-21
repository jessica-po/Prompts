from collections import namedtuple
from operator    import itemgetter

Friend = namedtuple("Friend", "m s")

n, d = list(map(int, input().split()))
f = [ ]
for i in range(n):
    f.append(Friend(*list(map(int, input().split()))))
f.sort(key=itemgetter(0))
left = 0
cur = f[0].s
result = cur
for i, fr in enumerate(f[1:], 1):
    while left < i and f[left].m + d <= fr.m:
        cur -= f[left].s
        left += 1
    cur += fr.s
    result = max(result, cur)
print(result)