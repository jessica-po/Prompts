def Intersect(aa,bb,xx,yy):
    a=min(aa,bb)
    b=max(aa,bb)
    x=min(xx,yy)
    y=max(xx,yy)
    
    if(a>=x and b<=y):
        return False
    if(x>=a and y<=b):
        return False
    if(b<=x):
        return False
    if(y<=a):
        return False
    return True

N=int(input())

case=False

L=list(map(int,input().split()))

for i in range(N-1):
    for j in range(i+1,N-1):
        if(Intersect(L[i],L[i+1],L[j],L[j+1])):
            case=True
if(case):
    print("yes")

else:
    print("no")