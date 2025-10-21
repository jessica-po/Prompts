import sys

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    a, b, c, d = nm()
    if a <= b:
        print(b)
    else:
        a -= b
        if c <= d:
            print(-1)
        else:
            print(b + c * ((a-1)//(c-d) + 1))
    return


# solve()

T = ni()
for _ in range(T):
    solve()