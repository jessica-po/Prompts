def solve():
    n, r = list(map(int, input().split()))
    k = min(r, n - 1)
    print(k * (k + 1) // 2 + (r >= n))


for i in range(int(input())):
    solve()