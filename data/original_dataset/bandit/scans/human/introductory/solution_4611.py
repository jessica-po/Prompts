N = int(input())

T = 0
X = 0
Y = 0

for i in range(N):
    t, x, y = list(map(int, input().split()))
    dt = t - T
    dx = abs(X - x)
    dy = abs(Y - y)
    dis = dx + dy
    if dt < dis:
        print("No")
        break
    if (dt - dis) % 2 == 1:
        print("No")
        break
    T = t
    X = x
    Y = y
else:
    print("Yes")