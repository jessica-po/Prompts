from itertools import *
def f(x):
    x -= 1
    ret = 0
    if x == 0:
        ret = 1
    else:
        while x != 0:
            ret += 1
            x //= 7
    return ret

def g(d):
    ret = 0
    for v in d:
        ret = ret * 7 + v
    return ret



n, m = list(map(int, input().split()))
a = f(n)
b = f(m)
if a + b > 7:
    print(0)
else:
    ans = 0
    for p in permutations(list(range(7)), a + b):
        if g(p[:a]) < n and g(p[a:]) < m:
            ans += 1
    print(ans)