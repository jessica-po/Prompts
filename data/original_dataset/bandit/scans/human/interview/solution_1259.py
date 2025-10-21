import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
e = [tuple(map(int, input().split())) for _ in range(m)]
g = [[] for _ in range(n + 1)]
for u, v in e:
    g[u].append(v)
    g[v].append(u)

req = 1
while req * req < n:
    req += 1

def dfs():
    dep = [0] * (n + 1)
    par = [0] * (n + 1)
    mk = [0] * (n + 1)
    st = [1]
    st2 = []
    while st:
        u = st.pop()
        if dep[u]:
            continue
        st2.append(u)
        dep[u] = dep[par[u]] + 1
        for v in g[u]:
            if not dep[v]:
                par[v] = u
                st.append(v)
            elif dep[u] - dep[v] + 1 >= req:
                ans = []
                while u != par[v]:
                    ans.append(u)
                    u = par[u]
                return (None, ans)
    while st2:
        u = st2.pop()
        if not mk[u]:
            for v in g[u]:
                if dep[v] < dep[u]:
                    mk[v] = 1
    return ([u for u in range(1, n + 1) if not mk[u]][:req], None)

iset, cyc = dfs()
if iset:
    print(1)
    print(*iset)
else:
    print(2)
    print(len(cyc))
    print(*cyc)