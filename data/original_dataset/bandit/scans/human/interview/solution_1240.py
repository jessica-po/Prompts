3

n = int(input())
l = []
r = []
for i in range(n):
    a, b = list(map(int, input().split()))
    l.append(a)
    r.append(b)

L = sum(l)
R = sum(r)
mx = abs(L - R)
k = 0
for i in range(n):
    Lp = L - l[i] + r[i]
    Rp = R - r[i] + l[i]
    if abs(Lp - Rp) > mx:
        mx = abs(Lp - Rp)
        k = i + 1

print(k)