def main():
    import sys
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    
    cnt = [0] * k
    for i in range(n):
        cnt[int(input()) - 1] += 1
    
    dead = 0
    ans = 0
    
    for i in cnt:
        if i & 1:
            dead += 1
            ans += i - 1
        else:
            ans += i
    
    if n & 1:
        print(ans + (dead + 1) // 2)
    else:
        print(ans + dead // 2)
    
    return 0

main()