def main():
    lst = list(tuple(map(int, input().split())) for _ in range(int(input())))
    res = []
    try:
        for a, b in reversed(lst):
            w, tmp = 1, ['(']
            while w < a:
                x = res.pop()
                w += len(x)
                tmp.append(x)
            if w > b:
                raise IndexError
            else:
                tmp.append(')')
                res.append(''.join(tmp))
    except IndexError:
        print('IMPOSSIBLE')
        return
    print(''.join(reversed(res)))


def __starting_point():
    main()

__starting_point()