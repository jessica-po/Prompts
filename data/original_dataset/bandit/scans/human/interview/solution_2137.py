n, A, C = list(map(int, input().split()))

def Ro(x, y):
    return A * x - y + C
 
huh = []
 
for i in range(n):
    z, x, y = list(map(int, input().split()))
    huh.append((Ro(x + z, z * A + y), x))
huh = sorted(huh)
anss = 0
c1 = 0
c2 = 0
prev = (-9999999999999, -999999999999999)
g = []

huh.append((-9999999999999, -999999999999999))
#print(huh)
for huhh in huh:
    if huhh[0] != prev[0]:
        g.append(c1)
        #print(g)
        for j in g:
            anss += (c2 - j) * j
        g = []
        c1 = 1
        c2 = 1
        prev = (huhh[0], huhh[1])
        continue
    c2 += 1
    if huhh[1] != prev[1]:
        g.append(c1)
        c1 = 0
        prev = (huhh[0], huhh[1])
    c1 += 1
print(anss)