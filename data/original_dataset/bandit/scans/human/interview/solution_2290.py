import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())

Edge = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

used = set()
ans = 0
mp = -1
for i in range(N):
    if i in used:
        continue
    if mp >= i:
        ans += 1
        Edge[mp].append(i)
        Edge[i].append(mp)
        mp = max(mp, i)
    else:
        st = i
    
    stack = [i]
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if vf not in used:
                mp = max(mp, vf)
                used.add(vf)
                stack.append(vf)

print(ans)