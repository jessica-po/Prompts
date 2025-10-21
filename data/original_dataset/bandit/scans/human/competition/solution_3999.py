from collections import defaultdict
N, = list(map(int, input().split()))

def normal(xs):
    return tuple(min((xs[j:] + xs[:j] for j in range(1, 5))))

dd = defaultdict(int)
cc = dict()
norm = dict()
ss = []
for _ in range(N):
    xs = list(map(int, input().split()))
    cnd = [tuple(xs[j:] + xs[:j]) for j in range(1, 5)]
    x = min(cnd)
    for item in cnd:
        norm[item] = x
    dd[x] += 1
    cc[x] = (4 if x[0] == x[1] else 2)if x[0] == x[2] and x[1] == x[3] else 1
    ss.append(x)

def icr(x):
    dd[x] += 1

def dcr(x):
    dd[x] -= 1

def f(ff, gg):
    a,b,c,d=ff
    e,h,g,f=gg
    tl = [(a,e,f,b), (b,f,g,c), (c,g,h,d), (d,h,e,a)]
    for cp in tl:
        if cp not in norm:
            return 0
    r = 1
    for cp in tl:
        cp = norm[cp]
        r *= dd[cp]*cc[cp]
        dcr(cp)
    for cp in tl:
        cp = norm[cp]
        icr(cp)
    return r

r = 0
for i in range(N):
    ff = ss[i]
    dcr(ff)
    for j in range(i+1, N):
        sl = ss[j]
        dcr(sl)
        x, y, z, w = sl
        sls = [(x,y,z,w), (y,z,w,x), (z,w,x,y), (w,x,y,z)]
        for s in sls:
            r += f(ff, s)
        icr(sl)
    icr(ff)
print((r//3))