#!/usr/bin/env python3

def main():
    import sys

    readln = sys.stdin.readline
    try:
        while True:
            n, k = list(map(int, input().split()))
            a = [['0'] * n for i in range(n)]
            i = j = 0
            while k > 0:
                if i == j:
                    a[i][j] = '1'
                    k -= 1
                    j += 1
                elif k >= 2:
                    a[i][j] = a[j][i] = '1'
                    k -= 2
                    j += 1
                elif i != n - 1:
                    a[i + 1][i + 1] = '1'
                    k = 0
                else:
                    assert a[i][i] == '1'
                    a[i][i] = '0'
                    a[i][j] = a[j][i] = '1'
                    k = 0

                if j == n:
                    i += 1
                    if i == n and k > 0:
                        print(-1)
                        break
                    j = i
            else:
                for row in a:
                    print(' '.join(row))

    except EOFError:
        pass

main()