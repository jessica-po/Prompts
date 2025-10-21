q = int(input())
for z in range(q):
    n, k = map(int, input().split())
    x = n // k
    n -= x * k
    m = min(k // 2, n)
    print(x * k + m)