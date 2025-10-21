n = int(input())
s = list(map(int, input().split()))

ans = 0
x0 = 0
x1 = 0
for i in range(n):
    if s[i] == 1:
        x1 = max(x0, x1) + 1
    else:
        x0 = x0 + 1
    ans = max(x0, x1)
print(ans)