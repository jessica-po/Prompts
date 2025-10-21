import math
m,R=list(map(int,input().split()))

cord=math.sqrt(2*(R**2))
ans=0
unit=int(2*R)
x=(m)*(m/2)
for i in range(m):
    ans+=2*R*m
    ans+=(cord*(m-1))
    if(i==0 or i==m-1):
        if(m==1):
            continue
        ans+=cord*(m-2)
    else:
        if(m==1):
            continue
        ans+=cord*(m-3)
    #left
    left=(i-1)-1
    if(left<-1):
        left=-1
    ans+=(left+1)*(left/2)*unit
    #right
    r=(m-1)-(i)-2
    if(r<-1):
        r=-1
    ans+=(r+1)*(r/2)*unit
ans/=(m**2)
print(ans)