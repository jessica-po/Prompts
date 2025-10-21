m = 301000
ns = [0] * m
es = [0] * m
c = [0] * m
b = [0] * m
t = [0] * m
P = 0

def add(b, k):
    k = t[k]
    while k:
        e = es[k]
        if b[-1] > e: b[-1] = e
        b[e] += 1
        k = ns[k]

def delete(b):
   for i in range(b[m - 1], m + 1):
       if b[i]:
           b[i] -= 1
           b[-1] = i
           return i

def calc(k):
    nonlocal b
    q = 0
    b = [0] * m
    b[-1] = m
    take = rank - dn
    if take < 0: take = 0
    add(b, k)
    add(b, k - 1)
    for i in range(1, take + 1): q += delete(b)
    for i in range(k - 1): add(b, i)
    for i in range(k + 1, P + 1): add(b, i)
    for i in range(1, k - take + 1): q += delete(b)
    return q

n, k = list(map(int, input().split()))
rank = n - k + 1

if rank == 0:
    print('0')
    return

for i in range(1, n + 1):
    p, e = list(map(int, input().split()))
    if p > P: P = p
    c[p] += 1
    es[i], ns[i] = e, t[p]
    t[p] = i

dn = 0
for i in range(1, n + 1):
    if i > 1: dn += c[i - 2]
    if c[i] + c[i - 1] + dn >= rank and rank <= i + dn:
        u = calc(i)
        if i < n:
            dn += c[i - 1]
            v = calc(i + 1)
            if u > v: u = v
        if i < n - 1:
            dn += c[i]
            v = calc(i + 2)
            if u > v: u = v
        print(u)
        return
        
print('-1')