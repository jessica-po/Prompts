import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def solve():
    cs = [aa[0]]
    for a in aa[1:]: cs.append((cs[-1] + a) % md)
    # print(cs)

    inv = pow(n, md - 2, md)
    ans = []
    for k in range(1, n):
        cur = 0
        for i in range(1, n):
            if n - 1 - k * i < 0: break
            cur = (cur + cs[n - 1 - k * i]) % md
        cur = cur * inv % md
        ans.append(cur)
    ans.append(0)
    print(*ans)

md=998244353
n=II()
aa=LI()
aa.sort()
solve()