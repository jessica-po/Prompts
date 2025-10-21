t=int(input())
for tt in range(t):
    n,p=map(int,input().split())
    now=1
    ans=0
    while ans!=2*n+p:
        for i in range(now+1,n+1):
            if ans==2*n+p:
                break
            print(now,i)
            ans+=1
        now+=1