from collections import defaultdict, Counter
N = int(input())
B = list(map(int, input().split()))
C = list(map(int, input().split()))
Edge = defaultdict(list)
Edc = defaultdict(int)
for b, c in zip(B, C):
    if b > c:
        print(-1)
        return
    Edge[b].append(c)
    Edc[(b, c)] += 1
    if b != c:
        Edge[c].append(b)
Deg = Counter(B + C)
eul = 0
st = []
for k, v in list(Deg.items()):
    if v % 2:
        eul += 1
        st.append(k)
s, e = B[0], B[0]
if eul and eul != 2:
    print(-1)
    return
if eul:
    s, e = st[0], st[1]
ans = [s]
while True:
    vn = ans[-1]
    while True:
        vf = Edge[vn][-1]
        if Deg[vf] != 0 and Edc[(vn, vf) if vn < vf else (vf, vn)]:
            break
        Edge[vn].pop()
    vf = Edge[vn].pop()
    Deg[vn] -= 1
    Deg[vf] -= 1
    Edc[(vn, vf) if vn < vf else (vf, vn)] -= 1
    ans.append(vf)
    if not Deg[vf]:
        break
loop = defaultdict(list)
for a in ans:
    if Deg[a]:
        loopa = [a]
        while Deg[a]:
            vn = loopa[-1]
            while True:
                vf = Edge[vn][-1]
                if Deg[vf] != 0 and Edc[(vn, vf) if vn < vf else (vf, vn)]:
                    break
                Edge[vn].pop()
            vf = Edge[vn].pop()
            Deg[vn] -= 1
            Deg[vf] -= 1
            Edc[(vn, vf) if vn < vf else (vf, vn)] -= 1
            loopa.append(vf)
            if not Deg[vf]:
                break
        loop[a] = loopa
Ans = [] 
for a in ans:
    if loop[a]:
        Ans.extend(loop[a])
        loop[a] = []
    else:
        Ans.append(a)    
if len(Ans) != N:
    print(-1)
    return
print(*Ans)