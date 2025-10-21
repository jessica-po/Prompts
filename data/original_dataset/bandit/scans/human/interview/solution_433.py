n, a, b = list(map(int, input().split()))
ans = a + b
while ans < 0:
    ans += n
ans %= n
if ans == 0:
    print(n)
else:
    print(ans)