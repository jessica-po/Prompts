for _ in range(int(input())):
    s, a, b, c = list(map(int, input().split()))

    x = s // c
    x += b * (x // a)

    print(x)