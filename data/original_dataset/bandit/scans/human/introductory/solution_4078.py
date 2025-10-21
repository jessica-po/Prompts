from copy import deepcopy
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = [list(map(int,input().split())) for i in range(m)]
best1 = -1
best2 = -1
best3 = []
for i in range(n):
    tmp = 0
    tmp2 = 0
    tmp3 = []
    c = deepcopy(a)
    for j in range(m):
        x,y = b[j]
        x-=1;y-=1
        if x<= i and i <= y:
            continue
        for k in range(x,y+1):
            c[k] -= 1
        tmp3.append(j+1)
        tmp2 += 1
    kon = max(c)-min(c)
    if best1 < kon:
        best1 = kon
        best2 = tmp2
        best3 = tmp3
print(best1)
print(best2)
print(*best3)