def main():
    w, h, n = list(map(int, input().split()))
    res, vrt, hor = [], [], []
    vh = (vrt, hor)
    for i in range(n):
        s = input()
        x = int(s[2:])
        flag = s[0] == 'V'
        vh[flag].append(i)
        res.append([x, flag])
    dim = []
    for tmp, m in zip(vh, (h, w)):
        tmp.sort(key=lambda e: res[e][0])
        u = [None, [0]]
        dim.append(u)
        j = z = 0
        for i in tmp:
            x = res[i][0]
            if z < x - j:
                z = x - j
            j = x
            v = [u, res[i]]
            u.append(v)
            u = v
            res[i].append(u)
        v = [u, [m], None]
        u.append(v)
        dim.append(v)
        if z < m - j:
            z = m - j
        dim.append(z)
    l, r, wmax, u, d, hmax = dim
    whmax = [wmax, hmax]
    for i in range(n - 1, -1, -1):
        x, flag, link = res[i]
        u = whmax[flag]
        res[i] = u * whmax[not flag]
        link[0][2] = link[2]
        link[2][0] = link[0]
        v = link[2][1][0] - link[0][1][0]
        if u < v:
            whmax[flag] = v
    print('\n'.join(map(str, res)))


def __starting_point():
    main()

__starting_point()