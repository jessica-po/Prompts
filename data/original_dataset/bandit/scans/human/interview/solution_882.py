t=input()
s=input()
n=len(s)
h=[0]*(n+1)
h[0]=0
j=0
fa=[0]*(n+1)
for i in range(2,n+1) :
    while j and s[i-1]!=s[j]:
        #j=fa[j-1];
        j=fa[j];
    if s[i-1]==s[j]:
        j+=1
    fa[i]=j;
#print(fa)
l=list()
j=fa[n]
while(j>0):
    l.append(j)
    j=fa[j]


tmp=t 
t=s 
s=tmp 
n=len(s)
dp=[0]*(n)
m=[0]*n 
'''if len(s)<len(t):
    print(0)'''
    
for i in range(len(t)-1,len(s)):
    can=True
    for j in range(len(t)):
        if s[i-len(t)+1+j]=='?':
            continue
        if s[i-len(t)+1+j]!=t[j]:
            can=False
            break
    if can:
        dp[i]=1
        for d in l:
            d=len(t)-d
            dp[i]=max(dp[i],1+dp[i-d])
        if i-len(t)>=0:
            dp[i]=max(dp[i],m[i-len(t)]+1)
    m[i]=max(m[i-1],dp[i])
print(m[-1])