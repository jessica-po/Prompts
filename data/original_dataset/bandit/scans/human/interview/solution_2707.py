n,k=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
cons=int(5e5+1)
mod=10**9+7
tpa=[1 for i in range(cons)]
tpa[0]=1
for i in range(1,cons):
    tpa[i]=(tpa[i-1]*2)%mod
if k>n:
    print(tpa[n-1])
else:
    il=[[]for i in range(k+1)]
    for i in range(n):
        if l[i]<=k:
            il[l[i]].append(i)
    for i in range(k+1):
        if len(il[i])==0:
            print(tpa[n-1])
            break
    else:
        pi=-1
        dp=[-1 for i in range(n)]
        dp[0]=1
        si=max(il,key=lambda x:x[0])[0]
        s=1
        for i in range(1,si):
            dp[i]=tpa[i]
            s=(s+dp[i])%mod
        ci=[0 for i in range(k+1)]
        j=si
        i=0
        while j<n:
            if l[i]>k :
                s=(s-dp[i])%mod
                i+=1
            elif ci[l[i]]+1<len(il[l[i]]) and il[l[i]][ci[l[i]]+1]<=j:
                s=(s-dp[i])%mod
                ci[l[i]]+=1
                i+=1
            else:
                dp[j]=s
                pi=i
                s=(s+dp[j])%mod
                j+=1
        print(dp[n-1])