n = int(input())

bestP = 10**9
sol = 0
for i in range(0, n):
    a, p = list(map(int, input().split()))

    bestP = min(bestP, p)
    sol += a * bestP

print(sol)