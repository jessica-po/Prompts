import numpy as np
def eratosthenes(m):
    if m<2:
        return []
    dp=[True]*(m+1)
    sosu=[2]
    like=[0]*(m+1)#累積和
    like[3]=1
    for x in range(3,m+1,2):
        if dp[x]:
            sosu.append(x)
            if dp[(x+1)//2]==True and (x+1)//2%2==1:
                like[x]+=1
        for j in range(2*x, m+1, x):
            dp[j]=False
    return like

like=eratosthenes(10**5+1)
c = np.array(like).cumsum()
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    ans=c[r]-c[l-1]
    print(ans)