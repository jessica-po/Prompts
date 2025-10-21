import math
from collections import Counter

s = list(map(int, input()))
substr = input().rstrip()
t = list(map(int, substr))

m = len(s)
x, y = 0, m
z = (x + y) // 2
while z != x:
    if z + math.floor(math.log10(z)) + 1 <= m:
        x = z
    else:
        y = z
    z = (x + y)//2
m1 = z
k = math.floor(math.log10(m1)) + 1

D = Counter(s)
D.subtract(list(map(int, str(m1))))
D.subtract(t)
try:
    c1 = min(i for i in range(1, 10) if D[i] > 0)
    c2 = t[0]

    D[c1] -= 1
    _prefix = [c1]
    
    for c in range(c2):
        _prefix += [c] * D[c]
    _suffix = []
    for c in range(c2 + 1, 10):
        _suffix += [c] * D[c]
    num = ''.join([str(c2)] * D[c2])
    prefix = ''.join(map(str, _prefix))
    suffix = ''.join(map(str, _suffix))

    if c2 == 0:
        print((min(prefix + substr + num + suffix,
                  prefix + num + substr + suffix)))
    else:
        D[c1] += 1
        st = []
        for c in range(10):
            st += [c] * D[c]
        print((min(prefix + substr + num + suffix,
                  prefix + num + substr + suffix,
                  substr + ''.join(map(str, st)))))
except ValueError:
    print(substr + '0'*D[0])