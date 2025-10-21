def main():
    _, k, m = [int(x) for x in input().split()]
    a = []
    last = ("-1", 0)
    a.append(last)
    for ai in input().split():
        if last[0] == ai:
            last = (ai, last[1]+1)
            a[-1] = last
        else:
            last = (ai, 1)
            a.append(last)

        if last[1] == k:
            a.pop()
            last = a[-1]
    a.pop(0)

    s1 = 0
    while len(a) > 0 and a[0][0] == a[-1][0]:
        if len(a) == 1:
            s = a[0][1] * m
            r1 = s % k
            if r1 == 0:
                print(s1 % k)
            else:
                print(r1 + s1)
            return
        join = a[0][1] + a[-1][1]

        if join < k:
            break
        elif join % k == 0:
            s1 += join
            a.pop()
            a.pop(0)
        else:
            s1 += (join // k) * k
            a[0] = (a[0][0], join % k)
            a.pop()
            break

    s = 0
    for ai in a:
        s += ai[1]

    print(s*m + s1)


def __starting_point():
    main()
__starting_point()