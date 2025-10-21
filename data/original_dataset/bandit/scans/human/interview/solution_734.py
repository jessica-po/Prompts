n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
mx = a[-1]
t = 0
ans = 0;
for i in a:
    if i > 0:
        if i > t:
            t += 1
        ans += i - 1
ans -= mx - t
print(ans)