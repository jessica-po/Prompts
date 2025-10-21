h, w, n = map(int,input().split())

xy_pos = dict()

for i in range(n):
    a, b = map(int, input().split())
    for k in range(-2,1):
        for l in range(-2,1):
            x = (a-1) + k
            y = (b-1) + l
            if (0 <= x <=(h-1)-2) and (0 <= y <=(w-1)-2):
                xy = str(x) + "x" + str(y)
                if xy in xy_pos:
                    xy_pos[xy] += 1
                else:
                    xy_pos[xy] = 1

ans = [0]*10                    
for v in xy_pos.values():
    ans[v] += 1
ans[0] = (h-2)*(w-2) - sum(ans)
for i in range(10):
    print(ans[i])