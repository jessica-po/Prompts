import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    a, b, c, d = nm()
    m = 10**6 + 10
    l = [0]*m
    for i in range(a, b+1):
        l[i+b] += 1
        l[i+c+1] += -1
    for i in range(m-1):
        l[i] += l[i-1]
    for i in range(m-2, -1, -1):
        l[i] += l[i+1]
    print(sum(l[i+1] for i in range(c, d+1)))
    return

solve()

# T = ni()
# for _ in range(T):
#     solve()