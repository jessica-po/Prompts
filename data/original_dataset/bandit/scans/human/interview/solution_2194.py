class BIT():
    def __init__(self,n):
        self.BIT=[0]*(n+1)
        self.num=n

    def query(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

n,q=map(int,input().split())
a=list(map(int,input().split()))
bit=BIT(2**n)
for i in range(2**n):
    bit.update(i+1,a[i])
b=0

def Sum(r,xor):
    id=xor
    res=0
    if r==-1:
        return res
    for i in range(n,-1,-1):
        if r>>i &1:
            L=(id>>i)<<i
            R=L+(1<<i)-1
            res+=bit.query(R+1)-bit.query(L)
            id^=(1<<i)
    return res


for _ in range(q):
    query=tuple(map(int,input().split()))
    if query[0]==1:
        g,x,k=query
        x-=1
        x^=b
        bit.update(x+1,k-a[x])
        a[x]=k
    elif query[0]==2:
        k=query[1]
        b^=2**k-1
    elif query[0]==3:
        k=query[1]
        if k!=n:
            b^=2**k
    else:
        gl,l,r=query
        l-=1
        test=Sum(r,b)-Sum(l,b)
        print(test)