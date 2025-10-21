n = int(input()) + 1
a = list(map(int, input().split())) + [1 << 50]
l, p, r = [0] * n, list(range(n)), []

for i in range(int(input())):
    t = list(map(int, input().split()))
    if t[0] == 2:
        r.append(l[t[1] - 1])
    else:
        x = t[1] - 1
        s, d = [x], t[2]
        while True:
            if p[x] != x:
                x = p[x]
                s.append(x)
                continue
            if l[x] + d < a[x]:
                l[x] += d
                break
            d -= a[x] - l[x]
            l[x] = a[x]
            x += 1
            s.append(x)
        for j in s:
            p[j] = x
        
print('\n'.join(map(str, r)))