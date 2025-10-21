import math
a,b= list(map(int,input().split()))
n=a+b
ans,l=0,1
while l<=n:
    g= n//l
    if a<g or b<g:
        l= (n//g) +1
        continue
    r= n//g
    a_low = (a+g)//(g+1)
    a_high = a//g
    b_low=(b+g)//(g+1)
    b_high = b//g
    if (a_low <= a_high and b_low <= b_high):
        ans += max(0,min(r,a_high+b_high)- max(l,a_low +b_low)+1)

    l=r+1
print(ans)