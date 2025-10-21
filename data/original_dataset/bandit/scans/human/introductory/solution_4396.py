N = int(input())
x = [0] * N
u = [0] * N
for i in range(N):
    x[i], u[i] = list(map(str, input().split()))

ans = 0
for i in range(N):
    if u[i] == 'JPY':
        ans += float(x[i])
    else:
        ans += float(x[i]) * 380000

print(ans)