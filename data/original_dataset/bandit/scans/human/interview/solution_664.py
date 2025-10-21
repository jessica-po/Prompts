n = int(input())
a = list(map(int, input().split()))
d = []
for i in range(1, n):
    d.append(a[i] - a[i - 1])
d.append(a[0] - a[n - 1])
cnt = 0
for i in range(0, n):
    if d[i] < 0:
        cnt += 1
        pos = i
if cnt == 0:
    print(0)
elif cnt > 1:
    print(-1)
else:
    print(n - pos - 1)