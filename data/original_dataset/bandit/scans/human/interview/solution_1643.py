from sys import stdin
s=stdin.readline().strip()
dp=[0 for i in range(len(s)+2)]
ons=[0 for i in range(len(s)+2)]
zs=[0 for i in range(len(s)+2)]
for i in range(len(s)-1,-1,-1):
    if s[i]=="1":
        ons[i]+=1
    if(i!=len(s)-1):
        ons[i]+=ons[i+1]
z=0
for i in range(len(s)-1,-1,-1):
    if(s[i]=="1"):
        dp[i]=max(1+ons[i+1],z)
    else:
        dp[i]=max(dp[i+1]+1,1+ons[i+1])
        z=dp[i]
    zs[i]=z

ans=""    
for i in range(len(s)):
    if s[i]=="1":
        x=dp[i]
        y=1+dp[i+1]
        if x==y:
            ans+="0"
        else:
            ans+="1"
    else:
        ans+="0"
print(ans)