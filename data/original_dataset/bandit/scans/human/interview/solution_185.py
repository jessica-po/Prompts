n, k = list(map(int,input().split()))
if k == 1 or k == n:
    print(3 * n)
else:
    print(3 * n + min(k - 1, n - k))