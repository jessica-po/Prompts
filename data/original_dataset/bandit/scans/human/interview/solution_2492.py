import numpy as np
n,k = map(int,input().split())
a = np.array(list(map(int,input().split())))
a.sort()
posi = a[a>0]
zero = a[a==0]
nega = a[a<0]

def cnt(x):
    c = 0
    if x >= 0:
        c += len(zero)*n
    c += np.searchsorted(a, x // posi, side = 'right').sum()
    c += (n-np.searchsorted(a, (- x - 1) // (-nega), side = 'right')).sum()
    c -= np.count_nonzero(a * a <= x)
    return c // 2

l = - 10 ** 18
r = 10 ** 18
while l + 1 < r:
    m = (l + r) // 2
    if cnt(m) < k:
        l = m
    else:
        r = m
print(r)