s=input()
M={"A","H","I","M","O","T","U","V","W","X","Y"}
ans="YES"
n=len(s)
for i in range(len(s)//2):
    x=s[i]
    y=s[n-i-1]
    if(x!=y or x not in M):
        ans="NO"
        break
if(n%2==1):
    if(s[n//2] not in M):
        ans="NO"
print(ans)