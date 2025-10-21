n = int(input())
a = list(map(int, input().split()))
info = 0
i = 0
dir = 1
result = 0
while True:
    if info >= a[i]:
        info += 1
        a[i] = n + 1
    if info == n:
        break
    i += dir
    if i < 0 or i == n:
        dir = -dir
        i += dir
        result += 1
print(result)