from math import gcd, sqrt
a,b = map(int, input().split())
g = gcd(a,b)
d = {}
for i in range(2, int(sqrt(g))+1):
    while g%i==0:
        g//=i
        d[i] = d.get(i, 0)+1
if g>1:
    d[g] = 1
print(len(d)+1)