for zz in range(int(input())):
    n = int(input())
    ans = 0
    while n > 1:
        ans += 1
        cr = 2
        while n >= cr:
            n -= cr
            cr += 3
    print(ans)