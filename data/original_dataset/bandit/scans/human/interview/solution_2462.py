# for _ in range(1):
for _ in range(int(input())):
    # a, b = map(int, input().split())
    n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    x = 6 + 10 + 14
    if x + 1 > n:
        print('NO')
        continue
    y = n - x
    if y not in (6, 10, 14):
        print('YES')
        print(6, 10, 14, y)
        continue
    x += 1
    y -= 1
    if y == 0:
        print('NO')
    else:
        print('YES')
        print(6, 10, 15, y)