n,m = map(int,input().split())
s = [list(map(int,input().split())) for i in range(m)]
p = list(map(int,input().split()))
ans = 0
for i in range(2 ** n):
    t = ['off'] * n
    x = i
    j = 0
    while x > 0:
        if x % 2 != 0:
            t[j] = 'on'
        x = x // 2
        j += 1
    flg = True
    for j in range(m):
        z = 0
        for k in range(1,s[j][0]+1):
            if t[s[j][k]-1] == 'on':
                z += 1
        if z % 2 != p[j]:
            flg = False
            break
    if flg:
        ans += 1
print(ans)