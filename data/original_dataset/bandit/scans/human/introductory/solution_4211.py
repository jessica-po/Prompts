n=int(input())
l=list(map(int,input().split()))
ans=l[0]+l[n-2]
for i in range(n-2):
    ans+=min(l[i],l[i+1])
print(ans)