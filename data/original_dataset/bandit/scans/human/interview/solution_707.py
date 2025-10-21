import sys
input=sys.stdin.readline

def gcd(x,y):
    if y==0:
        return x
    if x<y:
        x,y=y,x
    return gcd(y,x%y)

n,m=map(int,input().split())
X=list(map(int,input().split()))
P=list(map(int,input().split()))
d=X[1]-X[0]
for i in range(2,n):
    d=gcd(d,X[i]-X[i-1])
for i,p in enumerate(P):
    if d%p==0:
        print('YES')
        print(X[0],i+1)
        break
else:
    print('NO')