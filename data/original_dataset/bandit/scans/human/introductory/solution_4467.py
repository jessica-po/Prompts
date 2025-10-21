N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]
ab.sort()
cd.sort()

g = [[] for _ in range(N)]

for i, pab in enumerate(ab):
    for j, pcd in enumerate(cd):
        if pab[0] < pcd[0] and pab[1] < pcd[1]:
            g[j].append([pab[1],i])
        
ans = 0
s = set()

for gg in g:
    gg.sort(reverse=True)
    for ggg in gg:
        if ggg[1] in s:continue
        else:
            ans += 1
            s.add(ggg[1])
            break
print(ans)