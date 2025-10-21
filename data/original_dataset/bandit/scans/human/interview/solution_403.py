import sys,math
n,x,y=list(map(int,input().split()))
z=list(map(int,input().split()))
z.sort()
ans=0
for i in range(n):
    if z[i]%2==0:
        if x>=z[i]//2:
            x-=z[i]//2
            ans+=1
        else:
            z[i]-=x*2
            x=0
            y-=z[i]
            if y>=0:
                ans+=1
            else:
                break
    else:
        if x>=z[i]//2 and y>=1:
            x-=z[i]//2
            ans+=1
            y-=1
        elif x>=z[i]//2+1:
            x-=z[i]//2+1
            ans+=1
        else:
            z[i]-=x*2
            x=0
            y-=z[i]
            if y>=0:
                ans+=1
            else:
                break
print(ans)