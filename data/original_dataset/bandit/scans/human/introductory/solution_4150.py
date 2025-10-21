IN = input
rint = lambda: int(IN())
rmint = lambda: map(int, IN().split())
rlist = lambda: list(rmint())

n, k = rmint()
pr = [i for i in range(-1, n - 1)]
nx = [i for i in range(+1, n + 1)]
ans = [0] * n
p = [0] * n
i = 0
for g in rlist():
    p[n-(g-1)-1] = i
    i += 1


def dl(x, t):
    ans[x] = t
    if nx[x] < n: pr[nx[x]] = pr[x]
    if pr[x] >= 0: nx[pr[x]] = nx[x]


t = 1
for c in p:
    #print(ans)
    #print(pr)
    #print(nx)
    if ans[c]: continue
    dl(c, t)
    j = pr[c]
    for i in range(k):
        if j < 0: break
        dl(j, t)
        j = pr[j]
    j = nx[c]
    for i in range(k):
        if j >= n: break
        dl(j, t)
        j = nx[j]
    t = 3 - t
for o in ans: print(o, end='')