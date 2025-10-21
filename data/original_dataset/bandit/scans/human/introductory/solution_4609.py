n=int(input())
d=dict()
for _ in range(n):
    hoge=int(input())
    if d.get(hoge,0)==0:
        d[hoge]=1
    else:
        d[hoge]+=1
ans=0
for i in d.values():
    if i%2==1:
        ans+=1
print(ans)