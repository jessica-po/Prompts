n, m = map(int, input().split())
if m % n == 0:
    k = m // n
    res = 0
    while k % 2 == 0:
        k //= 2
        res += 1
    while k % 3 == 0:
        k //= 3
        res += 1
    if k > 1:
        print(-1)
    else:
        print(res)
else:
    print(-1)