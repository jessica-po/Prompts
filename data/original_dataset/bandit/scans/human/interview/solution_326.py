it = lambda: list(map(int, input().strip().split()))
INF = float('inf')


def solve():
    N = int(input())
    S = []
    R = []
    C = []
    for _ in range(N):
        s, c = input().strip().split()
        S.append(s)
        R.append(s[::-1])
        C.append(int(c))
    
    vis = set()
    mem = dict()

    def dp(s, p):
        if (s, p) in mem: return mem[s, p]
        if s == s[::-1]: return 0
        if (s, p) in vis: return INF

        ans = INF
        vis.add((s, p))
        for i, t in enumerate(S if p else R):
            if len(t) >= len(s) and t.startswith(s):
                ans = min(ans, dp(t[len(s):], p ^ 1) + C[i])
            elif len(s) > len(t) and s.startswith(t):
                ans = min(ans, dp(s[len(t):], p) + C[i])
        vis.discard((s, p))
        mem[s, p] = ans
        return ans
        
    ans = INF
    for i in range(N):
        ans = min(ans, dp(S[i], 0) + C[i])
    return -1 if ans == INF else ans


def __starting_point():
    ans = solve()
    print(ans)
__starting_point()