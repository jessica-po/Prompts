# python3


def readline(): return list(map(int, input().split()))


def solve(d):
    while d:
        dn = d.pop()
        if not d:
            for i in range(1, dn + 1):
                for j in range(i, dn + 1):
                    yield i, j + 1
            return
        else:
            d1 = d.pop(0)
            for i in range(1, dn + 1):
                for j in range(max(dn - d1 + 1, i), dn + 1):
                    yield i, j + 1

            d = [di - d1 for di in d]


def main():
    n, = readline()
    d = readline()

    assert len(d) == n

    edges = list(solve(d))
    print(len(edges))
    print("\n".join(map("{0[0]} {0[1]}".format, edges)))


main()