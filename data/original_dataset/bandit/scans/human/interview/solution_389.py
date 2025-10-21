a,b=list(map(int,input().split()))
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
def burn(n):
    c=0
    while(n%2==0):
        c+=1
        n=n//2
    while(n%3==0):
        c+=1
        n=n//3
    while(n%5==0):
        c+=1
        n=n//5
    return [c,n]
if(a==b):
    print(0)
else:
    g=gcd(a,b)
    c=a//g
    d=b//g
    l1=burn(c)
    l2=burn(d)
    if(l1[1]==1 and l2[1]==1):
        print(l1[0]+l2[0])
    else:
        print(-1)