def solve(n, l, s, www, children):
    ans = 0
    dp = [{} for _ in range(n)]
    for v in range(n - 1, -1, -1):
        cv = children[v]
        if not cv:
            dp[v][1] = www[v]
            continue
        ans += len(cv) - 1
        wv = www[v]
        if wv > s:
            return -1
        dv = dp[v]
        for c in cv:
            for lc, wc in list(dp[c].items()):
                if lc == l:
                    continue
                wt = wc + wv
                if wt > s:
                    continue
                if lc + 1 not in dv:
                    dv[lc + 1] = wt
                else:
                    dv[lc + 1] = min(dv[lc + 1], wt)
        if not dv:
            ans += 1
            dv[1] = wv

    return ans + 1


n, l, s = list(map(int, input().split()))
www = list(map(int, input().split()))
if n == 1:
    print(-1 if www[0] > s else 1)
    return
children = [set() for _ in range(n)]
for i, p in enumerate(map(int, input().split())):
    children[p - 1].add(i + 1)
print(solve(n, l, s, www, children))