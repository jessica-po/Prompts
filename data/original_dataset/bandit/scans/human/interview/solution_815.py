v1, v2, v3, vm = [int(k) for k in input().split(' ') if k]
minA = max(v3, vm)
maxA = 2 * min(v3, vm)
if maxA < minA:
    print(-1)
else:
    a = minA
    minB = max(v2, a + 1, 2 * vm + 1)
    maxB = 2 * v2
    if maxB < minB:
        print(-1)
        return
    b = minB
    minC = max(v1, b + 1, 2 * vm + 1)
    maxC = 2 * v1
    if maxC < minC:
        print(-1)
        return
    c = minC
    print(c)
    print(b)
    print(a)