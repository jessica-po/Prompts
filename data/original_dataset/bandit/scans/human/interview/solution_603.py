s=input().split()
for i in range(3):
    s[i]=int(s[i])
s.sort()


ans=s[0]//3 +s[1]//3 +s[2]//3

x=s[0]%3
y=s[1]%3
z=s[2]%3
if(x==0 and y==z==2 and s[0]!=0):
    ans+=1
if(y==0 and x==z==2 and s[1]!=0):
    ans+=1
if(z==0 and y==x==2 and s[2]!=0):
    ans+=1

ans+=min(x,y,z)
print(ans)