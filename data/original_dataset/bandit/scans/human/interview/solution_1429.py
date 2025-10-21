import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, S = input().split()
    N = int(N)
    ans = 0

    for i in range(N):
        a = 0
        c = 0
        for j in range(i, N):
            if S[j] == "A":
                a += 1
            elif S[j] == "T":
                a -= 1
            elif S[j] == "C":
                c += 1
            else:
                c -= 1

            if a == c == 0:
                ans += 1

    print(ans)


def __starting_point():
    main()

__starting_point()