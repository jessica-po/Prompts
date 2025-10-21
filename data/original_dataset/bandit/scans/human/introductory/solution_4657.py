from sys import stdin
c=int(stdin.readline().strip())
for cas in range(c):
    n,m=list(map(int,stdin.readline().strip().split()))
    s=list(map(int,stdin.readline().strip().split()))
    sm=0
    ans=[]
    ind=-1
    for i in range(n):
        if m==1:
            ind=i
            break
        sm+=s[i]
        if sm%2!=0:
            ans.append(i+1)
            sm=0
            m-=1
    if ind==-1:
        print("NO")
        continue
    sm=sum(s[ind::])
    if sm%2!=0:
        ans.append(n)
        print("YES")
        print(*ans)
    else:
        print("NO")