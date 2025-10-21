a,b = map(int,input().split())
ans = 0
for i in range(a,b+1):
    c = str(i)
    l = len(c)
    d = l // 2
    cnt = 0
    for i in range(d):
        if c[i] == c[-i-1]:
            cnt += 1
    if cnt == d:
        ans += 1
print(ans)