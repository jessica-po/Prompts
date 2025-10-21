from sys import stdin, stdout
input, print = stdin.readline, stdout.write
n = int(input())
r, g, b = [], [], []
ans = 0
for i in range(n):
    x, t = [i for i in input().split()]
    x = int(x)
    if t == 'P':
        g.append(x)
    elif t == 'R':
        r.append(x)
    else:
        b.append(x)
        
if len(g) == 0:
    if len(r):
        ans += r[-1] - r[0]
    if len(b):
        ans += b[-1] - b[0]
    print(str(ans))
    return
    
if not len(r):
    r.append(g[0])
if not len(b):
    b.append(g[0])
if r[0] < g[0]:
    ans += g[0] - r[0]
if b[0] < g[0]:
    ans += g[0] - b[0]
if r[-1] > g[-1]:
    ans += r[-1] - g[-1]
if b[-1] > g[-1]:
    ans += b[-1] - g[-1]
bi, ri = 0, 0

for i in range(len(g) - 1):
    while bi < len(b) - 1 and b[bi] < g[i]:
        bi += 1
    while ri < len(r) - 1 and r[ri] < g[i]:
        ri += 1
    a1, a2 = (g[i + 1] - g[i]) * 3, (g[i + 1] - g[i]) * 2
    mr, mb, cbi, cri = r[ri] - g[i], b[bi] - g[i], bi, ri

    while cbi + 1 < len(b) and b[cbi + 1] < g[i + 1]:
        mb = max(mb, b[cbi + 1] - b[cbi])
        cbi += 1
    mb = max(mb, g[i + 1] - b[cbi])
    while cri + 1 < len(r) and r[cri + 1] < g[i + 1]:
        mr = max(mr, r[cri + 1] - r[cri])
        cri += 1
    mr = max(mr, g[i + 1] - r[cri])
       
    if b[bi] < g[i] or b[bi] > g[i + 1]:
        a2 = 100000000000000
        a1 -= g[i + 1] - g[i]
        mb = 0
    if r[ri] < g[i] or r[ri] > g[i + 1]:
        a2 = 100000000000000
        a1 -= g[i + 1] - g[i]
        mr = 0
        
    ans += min(a1 - mr - mb, a2)
    
print(str(ans))