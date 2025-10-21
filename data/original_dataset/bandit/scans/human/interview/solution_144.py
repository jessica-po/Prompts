n = int(input())
a = list(map(int, list(input())))
for i in range(n - 1):
    sm = sum(a[:i + 1])
    tn = 0
    res = True
    has = False
    for j in range(i + 1, n):
        tn += a[j]
        if (tn == sm):
            tn = 0
            has = True
        elif tn > sm:
            res = False
            break
    if (tn == 0 and res and has):
        print("YES")
        break
else:
    print("NO")