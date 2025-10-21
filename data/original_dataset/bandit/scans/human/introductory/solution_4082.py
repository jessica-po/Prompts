n = int(input())
mass = list(map(int, input().split()))
left = [1] * n
right = [1] * n
for i in range(1, n):
    if mass[i] > mass[i - 1]:
        left[i] = left[i - 1] + 1
for i in range(n - 2, -1, -1):
    if mass[i] < mass[i + 1]:
        right[i] = right[i + 1] + 1
mx = 1
for i in range(n):
    if i == 0:
        mx = max(right[0], mx)
    elif i == n - 1:
        mx = max(mx, left[n - 1])
    elif mass[i + 1] > mass[i - 1]:
        mx = max(mx, left[i - 1] + right[i + 1])
    mx = max(mx, left[i])
    mx = max(mx, right[i])
print(mx)