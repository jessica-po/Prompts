n, m = list(map(int, input().split()))
p = list(map(int, input().split()))

for _ in range(m):
    l, r, x = list(map(int, input().split()))
    px = p[x - 1]
    cnt = l
    for i in range(l, r + 1):
        if p[i - 1] < px:
            cnt += 1
    if cnt == x:
        print("Yes")
    else:
        print("No")