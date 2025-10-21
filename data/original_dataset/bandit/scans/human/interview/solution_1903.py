n, m, d = list(map(int, input().split()))

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    b.append(list(map(int, input().split())))

a = sorted(a, key=lambda x: x[0] + (1- x[1] * 1e-10))
b = sorted(b, key=lambda x: x[0] + (1- x[1] * 1e-10))

tc, td = 0, 0

tc += a[-1][0]
tc += b[-1][0]
td += a[-1][1]
td += b[-1][1]

ai = n - 1
bi = m - 1

if td > d:
    print(0)
    return

while ai > 0:
    t = ai - 1
    if td + a[t][1] <= d:
        td += a[t][1]
        tc += a[t][0]
        ai -= 1
        continue
    else:
        break
    
cmax = tc

while bi > 0:
    bi -= 1
    tc += b[bi][0]
    td += b[bi][1]
    
    while td > d and ai < n:
        tc -= a[ai][0]
        td -= a[ai][1]
        ai += 1
    
    if ai == n:
        break
    
    if td <= d:
        cmax = max(cmax, tc)
        
print(cmax)