import sys
import heapq as hq

readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))

eps = 10**-7

def solve():
    n, k = nm()
    a = nl()
    ans = [0]*n
    ok = 10**9; ng = -4*10**18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        ck = 0
        for i in range(n):
            d =  9 - 12 * (mid + 1 - a[i])
            if d < 0:
                continue
            ck += min(a[i], int((3 + d**.5) / 6 + eps))
        # print(mid, ck)
        if ck > k:
            ng = mid
        else:
            ok = mid
    for i in range(n):
        d =  9 - 12 * (ok + 1 - a[i])
        if d < 0:
            continue
        ans[i] = min(a[i], int((3 + d**.5) / 6 + eps))
    # print(ans)
    rk = k - sum(ans)
    l = list()
    for i in range(n):
        if ans[i] < a[i]:
            hq.heappush(l, (-a[i] + 3 * ans[i]**2 - 3 * ans[i] + 1, i))
    for _ in range(rk):
        v, i = hq.heappop(l)
        ans[i] += 1
        if ans[i] < a[i]:
            hq.heappush(l, (-a[i] + 3 * ans[i]**2 - 3 * ans[i] + 1, i))
    print(*ans)
    return


solve()