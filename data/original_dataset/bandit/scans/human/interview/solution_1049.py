n,d = map(int,input().split())

ans = 0
has = 0
for i in range(d):
    s = input().count("1")
    if s==n:
        has = 0
    else:
        has+=1
    ans = max(ans,has)
print(ans)