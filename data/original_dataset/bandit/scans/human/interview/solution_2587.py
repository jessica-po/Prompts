# for _ in range(1):
for _ in range(int(input())):
    # a, b = map(int, input().split())
    n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    x = (n + 3) // 4
    y = n - x
    print(y * '9' + x * '8')