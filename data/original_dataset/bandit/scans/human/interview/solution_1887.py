n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))

r1 = r2 = 0
for i in range(n):
    r1, r2 = max(r1, r2 + h1[i]), max(r2, r1 + h2[i])

print(max(r1, r2))