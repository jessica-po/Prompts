n, k = map(int, input().split())
a = list(input()) * 2

iter1 = [0] * (2 * n)
iter2 = [0] * (2 * n)
changes = 0
for i in range(1, 2 * n):
    if a[i] != a[i - 1]:
        changes += 1
    else:
        changes = 0
    iter1[i] = changes
changes = 0
for i in range(2 * n - 2, -1, -1):
    if a[i] != a[i + 1]:
        changes += 1
    else:
        changes = 0
    iter2[i] = changes

iters = [min(iter1[n + i], iter2[i]) for i in range(n)]
for i in range(n):
    if iters[i] > n // 2:
        iters[i] = 10 ** 9 + 1
    it = min(iters[i], k)
    if it % 2 != 0:
        if a[i] == "B":
            a[i] = "W"
        else:
            a[i] = "B"
print("".join(a[:n]))