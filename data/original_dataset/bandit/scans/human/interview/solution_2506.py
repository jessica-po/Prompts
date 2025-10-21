import sys
import bisect
input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    
    l, r = -1, 10**6
    while r-l > 1:
        k = (r+l)//2
        count = 0
        for i in range(n):
            count += n-bisect.bisect_left(a, k-a[i])
        
        if count > m:
            l = k
        else:
            r = k
    ans = 0
    count = 0
    b = [0]*(n+1)
    for i in range(n):
        b[i+1] += b[i]+a[i]
    for i in range(n):
        index = bisect.bisect_left(a, r-a[i])
        ans += b[n]-b[index]+a[i]*(n-index)
        count += n-index
    
    if count < m:
        ans += (m-count)*l
    
    print(ans)
    
    
    
    
def __starting_point():
    main()

__starting_point()