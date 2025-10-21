n = input()
v = list(map(int, input().split()))

best = 1
current = 1
for i in range(1, len(v)):
    if v[i-1] <= v[i]:
        current += 1
    else:
        current = 1
    best = max(best, current)

print(best)