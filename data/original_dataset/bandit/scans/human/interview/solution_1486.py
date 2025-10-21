n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        print(a[1] - a[0], a[-1] - a[0])
    elif i == n - 1:
        print(a[i] - a[i - 1], a[i] - a[0])
    else:
        print(min(a[i + 1] - a[i], a[i] - a[i - 1]), max(a[-1] - a[i], a[i] - a[0]))