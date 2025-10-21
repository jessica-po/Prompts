def main():
    import sys
    input = sys.stdin.readline
    
    b = int(input())
    g = int(input())
    n = int(input())
    
    ans = n + 1
    if b < n:
        ans -= n - b
    if g < n:
        ans -= n - g
    
    print(ans)
    
    return 0

main()