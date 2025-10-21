n = int(input())
l = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

gcds = {0: 0}

for i in range(n):
    adds = {}
    for g in list(gcds.keys()):
        x = gcd(g, l[i])
        y = gcds.get(x)
        u = gcds[g]
        if y is not None:
            if u + c[i] < y:
                t = adds.get(x)
                if t and t > u + c[i] or t is None:
                    adds[x] = u + c[i]
        else:
            t = adds.get(x)
            if t and t > u + c[i]or t is None:
                adds[x] = u + c[i]
    gcds.update(adds)

if gcds.get(1):
    print(gcds[1])
else:
    print(-1)