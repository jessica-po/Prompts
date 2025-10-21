K, X = map(int, input().split())

lists = [X]

for i in range(1, K):
    if X + i <= 1000000:
        lists.append(X + i)
    if X - i >= -1000000:
        lists.append(X - i)

lists.sort()
print(*lists)