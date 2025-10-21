n = int(input())
l = list(map(int, input().split()))

total = sum(l)

gap = 0
for rod in l:
    gap = max(gap, rod - (total - rod))

print(gap + 1)