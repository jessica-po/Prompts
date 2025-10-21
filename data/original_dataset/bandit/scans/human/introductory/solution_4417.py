for ei in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = min(A) + k
    for i in A:
        if ans != -1 and abs(ans - i) > k:
            ans = -1
    print(ans)