n = int(input())
ans = 0
s = 0

while (n > 0):
    ans += 1
    s += ans
    n -= s

    if (n < 0):
        ans -= 1
        break

print(ans)