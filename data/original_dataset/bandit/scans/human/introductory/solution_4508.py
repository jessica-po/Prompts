from sys import stdin
n = int(stdin.readline())
g = dict()
for i in range(n-1):
    u,v = map(int,stdin.readline().split())
    g.setdefault(u-1,[]).append(v-1)
    g.setdefault(v-1, []).append(u-1)
st = [0]
rank = [0]*n
tree = [0]*n
msk = [0]*n
rd = dict()
while len(st)>0:
    top = st.pop()
    msk[top] = 1
    for c in g[top]:
        if msk[c] == 0:
            st.append(c)
            tree[c] = top
            rank[c] = rank[top]+1
            rd.setdefault(rank[c], []).append(c)
max_rank = max(rank)
reach = [0]*n
build = [0]*n
ans = 0
for r in range(max_rank, 2, -1):
    for node in rd[r]:
        if reach[node] == 0:
            reach[node] = 1
            reach[tree[node]] = 1
            reach[tree[tree[node]]] = 1
            build[tree[node]] = 1
print(sum(build))