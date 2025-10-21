for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, n, 2):
        a1 = a[i]
        a2 = a[i + 1]
        print(-a2, a1, end=" ")
    print()