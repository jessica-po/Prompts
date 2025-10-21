n, b = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = 0
for i in range(b):
    ans += min(x[i]-1, n-x[i]) + min(y[i]-1, n-y[i])
print(ans)