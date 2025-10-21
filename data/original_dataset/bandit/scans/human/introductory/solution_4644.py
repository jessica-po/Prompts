for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    a, b = 0, 0
    for elem in ar:
        if elem % 2 == 0:
            a = 1
        else:
            b = 1
    if sum(ar) % 2 == 1:
        print('YES')
    elif a == 1 == b:
        print('YES')
    else:
        print('NO')