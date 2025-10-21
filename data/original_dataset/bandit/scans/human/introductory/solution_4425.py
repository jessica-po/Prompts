n,k = map(int,input().split())

ans = 0

for i in range(1,n+1):
    if i>=k:
        ans += (1/n)
        continue
    x = 1
    while 1:
        i *= 2
        if i>=k:
            break
        else:x+=1
    ans += (1/n)*(1/2)**x
print(ans)