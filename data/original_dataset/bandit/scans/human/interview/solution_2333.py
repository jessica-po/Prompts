import  sys
import  math
input=sys.stdin.readline
#sys.setrecursionlimit(1000000)
mod=int(1000000007)
i=lambda :map(int,input().split())
n=int(input())
a=[int(x) for x in input().split()]
t=[[0]*21 for i in range(300005)]
for i in range(n):
    t[i][0]=a[i]

def build(n):
    for j in range(1,20):
        for i in range(n):
            if i+(1<<j)-1>n-1:
                break;
            t[i][j]=max(t[i][j-1],t[i+(1<<(j-1))][j-1])

def query(p,q):
    p,q=int(p),int(q)
    log=int(math.log2(q-p+1))
    m=t[p][log]
    n=t[q-(1<<log)+1][log]
    return max(m,n)

b=[-1]*(n+2)
build(n)
max1=-1
ans=0
for i in range(n):
    max1=max(max1,b[a[i]])
    b[a[i]]=i
    x=b[1]
    while x>max1:
        if x<=max1:
            break
        p=query(x,i)
        if p==i-x+1:
            ans+=1
            x=b[p+1]
        else:
            x=i-p+1
print(ans)