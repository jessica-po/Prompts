q = int(input())
for _ in range(q):
    l, r, d = list(map(int, input().split()))
    if d < l:
        print(d)
    else:
        v = d * (r // d)
        while v <= r:
            v += d
        print(v)