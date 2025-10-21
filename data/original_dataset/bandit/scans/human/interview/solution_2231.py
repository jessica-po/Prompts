import sys

rd = lambda : sys.stdin.readline().rstrip()

t = int(rd())
for _ in range(t):
    n = int(rd())
    a = list(map(int, rd().split()))
    b = []
    res_a, res_b = 1, 1e18
    
    a = sorted(a)
    i = 0
    while i < n-1:
        if a[i] == a[i+1]:
            b.append(a[i])
            i += 1
            
        i += 1
        
    p2s = lambda x, y : (x+y)**2/(x*y)
    
    for i in range(len(b)-1):
        if p2s(res_a, res_b) > p2s(b[i], b[i+1]):
            res_a, res_b = b[i], b[i+1]
            
    print(res_a, res_a, res_b, res_b)