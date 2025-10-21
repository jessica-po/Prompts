for _ in range(int(input())):
    n = int(input())
    r1 = list(map(int, input().split()))
    m = int(input())
    r2 = list(map(int, input().split()))
    o11 = sum(t % 2 for t in r1) # Counts odd number
    o12 = n - o11
    o21 = sum(t % 2 for t in r2) # Counts odd number
    o22 = m - o21
    print (o11 * o21 + o12 * o22)