n,k=map(int,input().split())
low=1
high=n
import sys
while low<=high:
    mid=(low+high)//2
    if mid*(mid+1)//2 -(n-mid)>k:
        high=mid-1
    elif mid*(mid+1)//2-(n-mid)==k:
        print(n-mid)
        return
    else :
        low=mid+1