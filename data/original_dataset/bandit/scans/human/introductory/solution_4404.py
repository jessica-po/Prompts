import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    y, m, d = list(map(int, S.split('/')))
    if m <= 4:
        print('Heisei')
    elif m > 4:
        print('TBD')

    return


def __starting_point():
    main()

__starting_point()