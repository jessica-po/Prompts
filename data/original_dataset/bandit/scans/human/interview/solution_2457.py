for _ in range(int(input())):
    n, a, b, c, d = tuple(map(int, input().split()))

    if (a - b) * n > c + d or (a + b) * n < c - d:
        print('No')
    else:
        print('Yes')