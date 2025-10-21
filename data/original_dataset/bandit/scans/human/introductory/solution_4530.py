from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=dd(int)
    for i in a:
        d[i]+=1
    ma=0
    r=len(d.keys())
    for i in d.keys():
        ma=max(ma,min(d[i]-1,r),min(d[i],r-1))
    print(ma)