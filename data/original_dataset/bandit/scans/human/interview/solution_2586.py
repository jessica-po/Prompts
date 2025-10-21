for _ in range(int(input())):
    n, m = map(int, input().split())
    print('W' + 'B' * (m - 1))
    print((('B' * (m) + '\n') * (n - 1))[:-1])