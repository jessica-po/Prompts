N = int(input())
Check = False
Sum = 0
Sum_l, Sum_r = 0, 0
for i in range(N):
    x, y = list(map(int, input().split()))
    Sum_l += x
    Sum_r += y
    Sum += x + y
    if (x % 2 + y % 2) % 2:
        Check = True
if Sum % 2:
    print(-1)
elif Sum_l % 2:
    if not Check:
        print(-1)
    else:
        print(1)
elif Sum_l % 2 == 0:
    print(0)