n = int(input())
a = list(map(int, input().split()))
i = 1
while i <= n - i + 1:
    if i % 2:
        a[i - 1], a[-i] = a[-i], a[i - 1]
    i += 1
print(*a)