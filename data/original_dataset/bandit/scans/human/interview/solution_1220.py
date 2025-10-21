n,m = list(map(int,input().split()))
ae = [[] for _ in range(n)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    ae[a-1].append(b-1)
    ae[b-1].append(a-1)
mn = -1
nbr = n
for i in range(n):
    if len(ae[i])<nbr:
        mn = i
        nbr = len(ae[i])
keep = ae[mn]
ok = n-len(keep)
while True:
    toDel = -1
    for i in keep:
        aeo = len(ae[i])
        for j in ae[i]:
            if j in keep:
                aeo -= 1
                if aeo<ok: break
        if aeo<ok:
            toDel = i
            break
    if toDel == -1:
        break
    else:
        keep.remove(i)
        ok += 1
out = [ok]
d = {}

if len(keep) == 1: out.append(1)
elif len(keep) == 0: out = out
else:
    keep.sort()
    for i in range(len(keep)):
        d[keep[i]] = i

    edg = [[] for _ in range(len(keep))]
    for i in range(len(keep)):
        for j in range(len(keep)):
            if i == j: continue
            edg[i].append(j)
            edg[j].append(i)

    for i in keep:
        for j in ae[i]: 
            if j in keep:
                if d[j] in edg[d[i]]: edg[d[i]].remove(d[j])
                if d[i] in edg[d[j]]: edg[d[j]].remove(d[i])
    used = [False]*len(keep)
    uss = 0
    while uss<len(keep):
        fi = -1
        for i in range(len(keep)):
            if not used[i]:
                fi = i
                break
        bfs = [fi]
        used[fi] = True
        usn = 1
        uss += 1
        while len(bfs) > 0:
            temp = bfs.pop()
            for i in edg[temp]:
                if not used[i]:
                    used[i] = True
                    bfs.append(i)
                    uss += 1
                    usn += 1
        out.append(usn)

out.sort()
print(len(out))
print(' '.join(map(str,out)))