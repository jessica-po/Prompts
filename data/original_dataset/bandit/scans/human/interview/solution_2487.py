n=int(input())
ki=[[] for _ in range(n)]
ans=0
for i in range(1,n+1):
    ans+=i*(n-i+1)

for _ in range(n-1):
    u,v=map(int,input().split())
    if u>v:u,v=v,u
    ans-=u*(n-v+1)
print(ans)