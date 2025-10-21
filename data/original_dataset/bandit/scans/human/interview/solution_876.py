n,k = list(map(int,input().split()));
a = list(map(int,input().split()));

if max(a) >= k:
    print(0)
    return

lx = 0
while a[lx] == 0:
    lx+=1

lo,hi = 1,k

def can(x):
    bc = 1
    tot = 0
    for i in range(n-lx):
        if(bc >= k):
            return True
        tot += bc*a[n-1-i]
        bc *= (x+i)
        bc = bc//(i+1)
        if(tot >= k):
            return True
    return tot >= k

while lo < hi :
    mid = (lo+hi)//2
    cancan = can(mid)
    #print(mid,cancan)
    if cancan : hi = mid
    else : lo = mid + 1

print(lo)