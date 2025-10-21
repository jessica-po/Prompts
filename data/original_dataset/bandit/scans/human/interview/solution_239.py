import math
n, m = list(map(int, input().split()))
if n == 0 : 
    print(0, 1)
    print(0, m)
    print(0, 0)
    print(0, m - 1)
elif m == 0 : 
    print(1, 0)
    print(n, 0)
    print(0, 0)
    print(n - 1, 0)
else :
    l = math.sqrt((n - 1) ** 2 + m ** 2) + math.sqrt(n ** 2 + m ** 2) + math.sqrt(n ** 2 + (m - 1) ** 2)
    l1 = max(m, n) + math.sqrt(n * n + m * m) * 2
    l2 = math.sqrt(n ** 2 + m ** 2) + math.sqrt((n - 1) ** 2 + m ** 2) * 2
    l3 = math.sqrt(n ** 2 + m ** 2) + math.sqrt((m - 1) ** 2 + n ** 2) * 2
    ans = max(l, l1, l2, l3)
    if l == ans :
        print(1, 0)
        print(n, m)
        print(0, 0)
        print(n, m - 1)
    elif l1 == ans :
        if n > m :
            print(n, m)
            print(0, 0)
            print(n, 0)
            print(0, m)
        else :
            print(n, m)
            print(0, 0)
            print(0, m)
            print(n, 0)
    elif l2 == ans :
        print(1, 0)
        print(n, m)
        print(0, 0)
        print(n - 1, m)
    else :
        print(0, 1)
        print(n, m)
        print(0, 0)
        print(n, m - 1)