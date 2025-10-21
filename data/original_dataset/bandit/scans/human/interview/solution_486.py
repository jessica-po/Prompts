n = int(input())
def p(x):
    ans = 1
    while x > 0:
        ans *= x % 10
        x //= 10
    return ans
ans = p(n)
for i in range(len(str(n))):
    cans = 9 ** i * p((n // 10 ** i) - 1)
    ans = max(ans, cans)
print(ans)