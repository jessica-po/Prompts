t = int(input())
for _ in range(t):
    n, x = [int(x) for x in input().split()]
    a = set([int(x) for x in input().split()])
    for i in range(1, 1000):
        if i in a:
            continue
        if x == 0:
            print(i - 1)
            break
        x -= 1