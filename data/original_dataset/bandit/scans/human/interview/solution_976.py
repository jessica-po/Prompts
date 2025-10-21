n, x = list(map(int, input().split()))
result = 0
cur = 1
for i in range(n):
    l, r = list(map(int, input().split()))
    result += r - l + 1
    result += (l - cur) % x
    cur = r + 1
print(result)