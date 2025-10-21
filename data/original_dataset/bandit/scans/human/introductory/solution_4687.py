n, k = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort()

num_sum = 0

for a, b in ab:
    num_sum += b
    if num_sum >= k:
        print(a)
        return