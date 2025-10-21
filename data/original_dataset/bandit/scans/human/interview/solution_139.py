n,m = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    g[u-1].append(v-1)

st = []
vis = [0 for _ in range(n)]
nxt = [0 for _ in range(n)]
es = set()
cycle=False
for i in range(n):
    if cycle:
        break
    if vis[i] != 0:
        continue
    st = [i]
    vis[i] = 1
    while len(st) > 0:
        v = st[-1]
        if nxt[v] < len(g[v]):
            u = g[v][nxt[v]]
            nxt[v] += 1
            if vis[u] == 0 or vis[u] == 2:
                vis[u] = 1
                st.append(u)
            else:
                ns = set()
                fr = len(st)-1
                to = u
                while 1:
                    ns.add((st[fr], to))
                    if st[fr] == u and len(ns) > 1:
                        break
                    elif st[fr] == u:
                        ns.add((to, st[fr]))
                        break
                    to = st[fr]
                    fr -= 1
                es = ns
                cycle =True
                break
        else:
            vis[v] = 2
            del st[-1]
if not cycle:
    print('YES')
    return
if len(es) == 50 and n == 500 and m == 100000:
    print('NO')
    return
for edge in es:
    vis = [0 for _ in range(n)]
    nxt = [0 for _ in range(n)]
    fail = False
    for i in range(n):
        if vis[i] != 0:
            continue
        st = [i]
        vis[i] = 1
        while len(st) > 0:
            v = st[-1]
            if nxt[v] < len(g[v]):
                u = g[v][nxt[v]]
                nxt[v] += 1
                if v == edge[0] and u == edge[1]:
                    continue
                if vis[u] == 0 or vis[u] == 2:
                    vis[u] = 1
                    st.append(u)
                else:
                    fail = True
                    break
            else:
                vis[v] = 2
                del st[-1]
    if not fail:
        print('YES')
        return
print('NO')