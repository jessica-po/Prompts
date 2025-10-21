def f(arr):
    d = max(arr)
    for i in range(len(arr)):
        arr[i] = d - arr[i]


# for _ in range(1):
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    # n = int(input())
    arr = list(map(int, input().split()))
    if k <= 2:
        for i in range(k):
            f(arr)
    elif k % 2 == 1:
        for i in range(3):
            f(arr)
    else:
        for i in range(4):
            f(arr)
    print(*arr)