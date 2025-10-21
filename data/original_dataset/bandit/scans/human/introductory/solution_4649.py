import sys
def countR(ip):
    c=0
    for i in ip:
        if(i=='R'):
            c+=1
    return c
    
def countB(ip):
    c=0
    for i in ip:
        if(i=='B'):
            c+=1
    return c
    
def countG(ip):
    c=0
    for i in ip:
        if(i=='G'):
            c+=1
    return c
# sys.stdin.readline()
t=int(sys.stdin.readline())
x='RGB'*680
y='GBR'*680
z='BRG'*680
for i in range(t):
    n,k=list(map(int,sys.stdin.readline().strip().split()))
    a=sys.stdin.readline().strip()
    xk=x[:k]
    yk=y[:k]
    zk=z[:k]
    # print(k,xk,zk)
    # xc=[]
    # yc=[]
    # zc=[]
    # xc.append(countR(xk))
    # xc.append(countG(xk))
    # xc.append(countB(xk))
   
    # yc.append(countR(yk))
    # yc.append(countG(yk))
    # yc.append(countB(yk))
    
    # zc.append(countR(zk))
    # zc.append(countG(zk))
    # zc.append(countB(zk))
    op=2001
    for j in range(n-k+1):
        b=a[j:j+k]
        # print(len(b),xc,zc)
        # bc=[]
        
        # bc.append(countR(b))
        # bc.append(countG(b))
        # bc.append(countB(b))
        xd=0
        yd=0
        zd=0
        # print(a,b,xc,yc,zc,bc)
        for jj in range(len(b)):
            if(b[jj]!=xk[jj]):
                xd+=1
            if(b[jj]!=yk[jj]):
                yd+=1
            if(b[jj]!=zk[jj]):
                zd+=1
         # print(a,b,xd,yd,zd,z)
        op=min(op,xd,yd,zd)
    print(op)