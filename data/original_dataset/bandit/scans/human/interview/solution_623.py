a,b=map(int,input().split())
ans=0
while a>0 and b>0:
    if max(a,b)>1: ans+=1
    if a<b: a+=3
    else: b+=3
    a-=2;b-=2
print(ans)