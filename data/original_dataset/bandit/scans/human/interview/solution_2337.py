n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, 0
while i < n:
    while j < m and b[j] < a[i]:
        j += 1
    if j == m:
        break
    j += 1
    i += 1
print(n - i)