for TT in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())
    l = max(-1, (b + c - a) // 2)
    r = c
    print(r - l if r >= l else 0)