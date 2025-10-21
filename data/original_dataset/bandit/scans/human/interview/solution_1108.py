n=int(input())
ans=0
for i in range(n):
    a,b=map(int,input().split())
    if b-a>=2: ans+=1
print(ans)