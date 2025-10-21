import sys


def main():
    n, q, c = list(map(int, sys.stdin.readline().split()))
    a = []
    c += 1
    for i in range(c):
        t = []
        for j in range(102):
            t.append([0] * 102)
        a.append(t)

    for i in range(n):
        x, y, s = list(map(int, sys.stdin.readline().split()))
        for j in range(c):
            a[j][x][y] += s
            s += 1
            if s >= c:
                s = 0

    for k in range(c):
        for i in range(102):
            for j in range(1, 102):
                a[k][i][j] += a[k][i][j - 1]

    alans = [0] * q
    for i in range(q):
        t, x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
        ans = 0
        t = t % c
        for j in range(x1, x2 + 1):
            ans += a[t][j][y2] - a[t][j][y1 - 1]

        alans[i] = str(ans)
    print("\n".join(alans))


main()