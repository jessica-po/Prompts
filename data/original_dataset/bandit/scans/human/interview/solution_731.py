import math
w,m,k=list(map(int,input().split()))

x=int("1"+("0"*len(str(m))))

h=x-m
n=len(str(m))

ans=w//(n*k)

if(ans>h):
    ans=h
    w-=h*n*k
    while(w>0):
        n+=1
        x=w//(n*k)
        if(x>=10**(n-1)*9):
            ans+=(10**(n-1))*(9)
            w-=(n*k*(10**(n-1))*(9))
        else:
            ans+=x
            break
print(ans)