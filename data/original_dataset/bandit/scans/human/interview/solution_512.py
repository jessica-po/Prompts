import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    L = 2 * N
    floor = [[0, 0] for _ in range(L)]
    com = dict()

    for i in range(1, N + 1):
        A, B = map(int, readline().split())
        com[i] = [-1, -1]
        if A != -1:
            if floor[A - 1][1] == 0:
                floor[A - 1] = [i, 1]
                com[i][0] = A - 1
            else:
                return print("No")
        if B != -1:
            if floor[B - 1][1] == 0:
                floor[B - 1] = [i, 2]
                com[i][1] = B - 1
            else:
                return print("No")
        if A != -1 and B != -1:
            if A >= B:
                return print("No")

    dp = [False] * (L + 1)

    if floor[0][1] == 2:
        return print("No")
    else:
        dp[0] = True

    for i in range(L):
        if not dp[i]:
            continue
        for j in range(i + 1, L, 2):
            ok = True
            w = (j - i + 1) // 2
            for k in range(w):
                p = i + k
                q = i + w + k
                if floor[p][1] == 2 or floor[q][1] == 1:
                    ok = False
                if floor[p][1] == 1 and floor[q][1] == 2:
                    if floor[p][0] != floor[q][0]:
                        ok = False
                if floor[p][1] == 1:
                    f = floor[p][0]
                    if com[f][1] != q and com[f][1] != -1:
                        ok = False
                if floor[q][1] == 2:
                    f = floor[q][0]
                    if com[f][0] != p and com[f][0] != -1:
                        ok = False
            if ok:
                dp[j + 1] = True

    print("Yes") if dp[L] else print("No")


def __starting_point():
    main()

__starting_point()