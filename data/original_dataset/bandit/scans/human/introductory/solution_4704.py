import sys
import itertools

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

N = ini()
A = inl()


def solve():
    B = list(itertools.accumulate(A, initial=0))
    s = 0
    ans = 10 ** 12
    for i in range(N - 1, 0, -1):
        s += A[i]
        ans = min(ans, abs(s - B[i]))

    return ans


print(solve())