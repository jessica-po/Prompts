n, m = list(map(int, input().split()))
table = [False] * (n + 1)
for _ in range(m):
    a, b = list(map(int, input().split()))
    table[a] = table[b] = True
print(n - 1)
for i in range(1, n + 1):
    if not table[i]:
        for j in range(1, n + 1):
            if i != j:
                print(i, j)
        break