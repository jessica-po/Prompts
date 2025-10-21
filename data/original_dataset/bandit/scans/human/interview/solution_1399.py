#      
import    sys 
 
def getIntList():
    return list(map(int, input().split()))    
 


 
N, = getIntList()

zp = []
for i in range(N):
    ax, ay, bx, by  = getIntList()
    if ax>bx:
        ax,bx = bx,ax
        ay,by = by, ay
    zp.append( (ax,ay, bx,by))
  
res = 0
def gcd(a,b): 
    if b==0:return a
    return gcd(b, a%b)
zgcd = []
for i in range(N):
    ax, ay, bx, by = zp[i]
    tx =  abs(bx-ax)
    ty = abs(by - ay)
 
    g = gcd(tx, ty)
    res += g+1
 
    zgcd .append(g)
 
"""
ax + k1 dax = bx + k2 dbx
ay + k1 day = by + k2 dby
"""
for i in range(N):
    ax = zp[i][0]
    dax = (zp[i][2] - ax) // zgcd[i]
    ay = zp[i][1]
    day = (zp[i][3] - ay) // zgcd[i]
    cross = []
    for j in range(i+1, N):
        #dprint('node',i,j)
        bx = zp[j][0]
        dbx = (zp[j][2] - bx) // zgcd[j]
        by = zp[j][1]
        dby = (zp[j][3] - by) // zgcd[j]
        #dprint(ax,dax,ay,day)
        #dprint(bx,dbx,by,dby)
        t1 = ax * day - ay * dax - bx * day + by * dax
        t2 = dbx *day - dby * dax
        
        #dprint(t1,t2)
        if t2==0:
            continue
        if t1%t2!=0:
            continue
        k2 = t1 // t2
        if k2 <0 or k2 > zgcd[j]:
            continue
        if dax!=0:
            t3 = k2*dbx + bx - ax
            if t3%dax!=0:
                continue
            k1 = t3//dax
        else:
            t3 = k2* dby + by - ay
            if t3%day !=0:
                continue
            k1 = t3//day
        if k1<0 or k1 > zgcd[i]:
            continue
        #dprint(ax + k1 * dax, ay+k1 * day)
        cross.append(k1)
    if not cross: continue
    cross.sort()
 
    d = 1
    for j in range(1, len(cross)):
        if cross[j]!=cross[j-1]:
            d+=1
    res-=d
print(res)