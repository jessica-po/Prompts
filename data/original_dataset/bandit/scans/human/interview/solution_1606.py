from functools import reduce
def main():
    from sys import stdin
    from operator import xor
    from functools import reduce
    x, res = reduce(xor, (input()[i] == '1' for i in range(0, int(input()) * 2, 2))), []
    input()
    for s in stdin.read().splitlines():
        if s == '3':
            res.append("01"[x])
        else:
            x ^= True
    print(''.join(res))


def __starting_point():
    main()

__starting_point()