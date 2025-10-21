s=input()
dp0=[0]*(len(s)+1)
dp1=[0]*(len(s)+1)
dp1[0]=1
for i in range(1,len(s)+1):
  n=int(s[i-1:i])
  dp0[i]=min(dp0[i-1]+n,dp1[i-1]+10-n)
  dp1[i]=min(dp0[i-1]+(1 if n+1==10 else n+1),dp1[i-1]+10-n-1)
print(dp0[-1])