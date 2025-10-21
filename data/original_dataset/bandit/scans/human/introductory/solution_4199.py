n, limit = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
for i in range(n):
    if lst[i] >= limit:
        count += 1

print(count)