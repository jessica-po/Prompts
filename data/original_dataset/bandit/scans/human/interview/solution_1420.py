n, l = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

result = 0
for i in range(1, n):
    result = max(result, (a[i] - a[i - 1]) / 2)
result = max(result, a[0])
result = max(result, l - a[-1])
print(result)