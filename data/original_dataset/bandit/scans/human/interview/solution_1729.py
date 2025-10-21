n, q = list(map(int, input().split()))
s = input()
for _ in range(q):
    l, r = list(map(int, input().split()))
    t = list(s[l-1:r])
    p, d = 0, 1
    res = [0] * 10
    while 0 <= p < len(t):
        if '0' <= t[p] <= '9':
            k = int(t[p])
            res[k] += 1
            if k > 0:
                t[p] = str(k-1)
                p += d
            else:
                t.pop(p)
                if d == -1:
                    p += d
        else:
            d = -1 if t[p] == '<' else 1
            if 0 <= p+d < len(t) and not ('0' <= t[p+d] <= '9'):
                t.pop(p)
                if d == -1:
                    p += d
            else:
                p += d
    print(*res)