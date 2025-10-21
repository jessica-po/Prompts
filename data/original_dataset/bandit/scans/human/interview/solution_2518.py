import heapq

n, a, b = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))
ac = (max(h) - 1) // b + 1
wa = 0
while ac - wa > 1:
    wj = (ac + wa) // 2
    num = 0
    for i in range(n):
        num += max((h[i] - b * wj - 1) // (a - b) + 1, 0)
    if num <= wj:
        ac = wj
    else:
        wa = wj
print(ac)