a, b = map(int, input().split())
a = min(a, b)
ans = 1
for i in range(1, a + 1):
    ans *= i
print(ans)