for _ in range(int(input())):
    n = int(input())
    # arr = list(map(int, input().split()))
    # n, m = map(int, input().split())
    arr = []
    x = 1
    while n > 0:
        if (n % 10):
            arr.append((n % 10) * x)
        n //= 10
        x *= 10
    print(len(arr))
    print(*arr)