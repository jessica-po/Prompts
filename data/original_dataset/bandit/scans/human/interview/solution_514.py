t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    if (1 - n) ** 2 - 4 * (d - n) >= 0:
        print('YES')
    else:
        print('NO')