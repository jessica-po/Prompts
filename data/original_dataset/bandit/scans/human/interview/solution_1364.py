mi = lambda: [int(i) for i in input().split()]

n = int(input())
t = mi()

a = []
v = 0
c = 0

for i in t:
    if i == v:
        c += 1
    else:
        if c != 0:
            a.append(c)
        c = 1
        v = i
a.append(c)

r = 0
for k in range(1, len(a)):
    r = max(r, min(a[k - 1], a[k]) * 2)
print(r)