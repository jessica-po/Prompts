import bisect

N,M,X = map(int,input().split())
A = list(map(int,input().split()))

index = bisect.bisect_left(A,X)
ans = min(M-index,index)
print(ans)