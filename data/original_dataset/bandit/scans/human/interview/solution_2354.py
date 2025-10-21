import sys

n, q = map(int, sys.stdin.readline().rstrip().split())
for _ in range(q):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x, y = x-1, y-1
    
    if (x+y)%2 == 0:
        res = 1
        res += x//2 * n
        res += x%2 * ((n+1)//2)
        res += y//2

        print(res)
    else:
        res = (n*n+1)//2+1
        res += x//2 * n
        res += x%2 * ((n)//2)
        res += y//2

        print(res)