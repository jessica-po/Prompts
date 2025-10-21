n,m,k = (int(i) for i in input().split())
r = []
for i in range(m):
    u,v,p = (int(i) for i in input().split())
    r += [(p,u,v)]
if k == 0:
    print(-1)
    return
else:
    s = list(map(int,input().split()))
    sklad = [False]*n
    for i in range(len(s)):
        sklad[s[i]-1] = True
        
    ans = 10**10
    for i in range(len(r)):
        if sklad[r[i][1]-1] != sklad[r[i][2]-1]:
            ans = min(ans,r[i][0])
            
if ans == 10**10:
    print(-1)
else:
    print(ans)