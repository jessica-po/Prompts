n=int(input())
l1=list(map(int,input().split()))
l1.sort()
l1=l1[::-1]
ans=[-1]*n
i=0
y=n-1
for j in range(n):
    if j%2==0:
        ans[i]=l1[j]
        i+=1
    else :
        ans[y]=l1[j]
        y-=1
flag=0
for i in range(n):
    if ans[i]>=ans[i-1]+ans[(i+1)%n]:
        flag=1
        break
if flag==0:
    print("YES")
    print(' '.join(str(x) for x in ans))
else :
    print("NO")