n, a, b = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    val = 0
    for c in str(i):
        val += int(c)
    if a <= val <= b:
        ans += i
print(ans)