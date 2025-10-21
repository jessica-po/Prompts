for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    ans = "NO"
    for i in range(1, n):
        if ar[i] == ar[i - 1]:
            ans = 'YES'
            break
    print(ans)