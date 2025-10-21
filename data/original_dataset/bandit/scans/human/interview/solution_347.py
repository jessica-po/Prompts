m = list(map(int, input().split()))
w = list(map(int, input().split()))
a = [500, 1000, 1500, 2000, 2500]
v = list(map(int, input().split()))
ans = 0
for i in range(len(m)):
    ans += max(0.3 * a[i], (1 - m[i] / 250) * a[i] - 50 * w[i])
ans += v[0] * 100
ans -= v[1] * 50
print(int(ans))