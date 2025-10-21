n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
mc = sorted(((y, x) for x, y in enumerate(c)), reverse=True)
for _ in range(m):
    t, d = map(int, input().split())
    t -= 1
    if a[t] >= d:
        print(c[t] * d)
        a[t] -= d
    else:
        x = a[t] * c[t]
        d -= a[t]
        a[t] = 0
        while d:
            if not mc:
                print(0)
                break
            cost, index = mc[-1]
            if a[index] >= d:
                x += cost * d
                a[index] -= d
                d = 0
            else:
                x += cost * a[index]
                d -= a[index]
                a[index] = 0
            if a[index] == 0:
                mc.pop()
        else:
            print(x)