def solve():
    n = int(input())
    A = [int(k) for k in input().split()]
    
    A.sort()
    
    ans = 0
    
    for i in range(0,n,2):
        ans += (A[i+1] - A[i])
        
    print (ans)
    
solve()