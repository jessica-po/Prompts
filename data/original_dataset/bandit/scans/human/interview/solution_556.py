l, r, n = map(int, input().split())
a = n
n = 1
cnt = 0
while n <= r:
    if n >= l:
        cnt += 1
        print(n, end=' ')
    n *= a
if cnt == 0:
    print(-1)