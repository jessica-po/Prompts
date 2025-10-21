n = int(input())
lcnt = 0
rcnt = 0
for i in range(n):
    x, y = map(int, input().split())
    if x < 0:
        lcnt += 1
    else:
        rcnt += 1

if (lcnt <= 1 or rcnt <= 1):
    print("Yes")
else:
    print("No")