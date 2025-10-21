q = int(input())
for _ in range(q):
    a, b = list(map(int, input().split()))
    print((b - a % b) % b)