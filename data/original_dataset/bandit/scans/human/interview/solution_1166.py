import sys


def __starting_point():
    cin = sys.stdin

    n = int(next(cin))
    a = list(map(int, next(cin).split()))

    n2idx = {a[i]: i for i in range(n)}

    f = [False] * (n+1)

    for i in range(n, 0, -1):
        idx_lg = n2idx[i]

        win_flag = False
        for j in range(idx_lg%i, n, i):
            if a[j] > i and not f[a[j]]:
                win_flag = True
                break
        f[i] = win_flag
        
    f = ''.join(['A' if f[a_i] else 'B' for a_i in a])
    print(f, flush=True)

__starting_point()