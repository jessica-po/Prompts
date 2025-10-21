def main():
    l = []
    for i in range(int(input())):
        y, n, m = 1989, 0, 1
        for d in input()[-1:3:-1]:
            n += (ord(d) - 48) * m
            m *= 10
            t = n - y % m
            y += (m + t if t < 0 else t) + m
        l.append(y - m)
    print('\n'.join(map(str, l)))


def __starting_point():
    main()

__starting_point()