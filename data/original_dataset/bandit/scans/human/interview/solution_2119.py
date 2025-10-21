def kmp(pat,text,t):
    s=pat+"?"+text;
    #z[i] es el tamaño del prefijo mas largo de, formado por una subcadena s[i:...]
    z=[0 for i in range(len(s))]
    L=0;R=0;n=len(s);
    for i in range(1,len(s)):
        if i>R:
            L=R=i
            while R<n and s[R-L]==s[R]:
                R+=1
            z[i]=R-L
            R-=1
        elif z[i-L]+i<=R:
            z[i]=z[i-L]
        else:
            L=i
            while R<n and s[R-L]==s[R]:
                R+=1
            z[i]=R-L
            R-=1
    for i in range(len(pat)+1,len(z)):
        dp[t][i-(len(pat)+1)]=z[i]%len(pat)
from sys import stdin
mod=998244353
a=stdin.readline().strip()
l=stdin.readline().strip()
r=stdin.readline().strip()
x=len(l)
y=len(r)
n=len(a)
dp=[[0 for i in range(len(a))]for j in range(2)]
ans=[0 for i in range(len(a)+1)]
ans[-1]=1
kmp(l,a,0)
kmp(r,a,1)
auxl=x-1
auxr=y-1
acum=[0 for i in range(n+2)]
acum[n]=1
for i in range(n-1,-1,-1):
    if a[i]=="0":
        if l[0]=="0":
            ans[i]=ans[i+1]
        acum[i]=(acum[i+1]+ans[i])%mod
        continue
    if auxl>=n:
        acum[i]=(acum[i+1]+ans[i])%mod
        continue
    if auxl!=auxr:
        if (auxl+i)<n and a[dp[0][i]+i]>=l[dp[0][i]]:
            ans[i]=(ans[i]+ans[i+auxl+1])%mod
        if (auxr+i)<n and a[dp[1][i]+i]<=r[dp[1][i]]:
            ans[i]=(ans[i]+ans[i+auxr+1])%mod
    else:
        if (auxl+i)<n and a[dp[0][i]+i]>=l[dp[0][i]] and a[dp[1][i]+i]<=r[dp[1][i]]:
            ans[i]=(ans[i]+ans[i+auxl+1])%mod
    lim1=auxl+i+2
    lim2=min(auxr+i+1,n+1)
    if lim1<lim2:
        ans[i]=(ans[i]+acum[lim1]-acum[lim2])%mod
    acum[i]=(acum[i+1]+ans[i])%mod
print(ans[0]%mod)