def main():
    import sys
    input = sys.stdin.readline
    
    n, l, r = map(int, input().split())
    
    mi = 0
    curr = 1 << l - 1
    for i in range(n):
        mi += curr
        if curr != 1:
            curr >>= 1
    
    ma = 0
    curr = 1
    for i in range(n):
        ma += curr
        if curr != 1 << r - 1:
            curr <<= 1
    
    print(mi, ma)
    
    return 0

main()