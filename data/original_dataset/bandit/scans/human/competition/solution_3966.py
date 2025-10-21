n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
if n == 1:
    ans = a[0]
else:
    mult = 2
    for i in range(n - 1):
        ans += mult * a[i]
        mult += 1
    ans += (mult - 1) * a[-1]
print(ans)