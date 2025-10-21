import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    patties=[0]*n
    mx=0
    for p in a:
        patties[p-1]+=1
        mx=max(patties[p-1],mx)
    mxs=0
    for p in patties:
        if p==mx:
            mxs+=1
    rest=n-mx
    rest-=mxs
    rest+=1
    spots=mx-1
    print(rest//spots)