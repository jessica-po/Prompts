tst = int(input())
for i in range(0, tst):
    n = int(input())
    ans = 1
    l = 1
    p = []
    while l <= n:
        ans += 1
        l = n // (n // l)
        p.append(n // l)
        l += 1
    p.append(0)
    p.reverse()
    print(len(p))
    print(" ".join(str(x) for x in p))