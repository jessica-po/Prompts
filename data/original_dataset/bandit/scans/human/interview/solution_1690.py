rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

def solve(N, A):
    ans = 0
    prev = float('inf')
    for x in reversed(A):
        x = min(x, prev - 1)
        ans += max(x, 0)
        prev = x
    return ans

for tc in range(1):#rri()):
    N = rri()
    A = rrm()
    print(solve(N, A))