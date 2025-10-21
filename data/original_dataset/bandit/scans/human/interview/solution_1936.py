t = int(input())
while t:
    l, r = list(map(int, input().split()))
    if l * 2 <= r:
        print(l, 2 * l)
    else:
        print(-1, -1)
    t -= 1