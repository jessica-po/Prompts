n=int(input())
a=list(map(int,input().split()))
count=[0]*(10**5+1)
for i in a:
    count[i]+=1
ans=[]
for i in range(10**5+1):
    if count[i]:
        ans.append(i)
        count[i]-=1
if len(ans)!=n:
    for i in reversed(range(10**5+1)):
        if count[i] and ans[-1]!=i:
            ans.append(i)
print(len(ans))
print(*ans)