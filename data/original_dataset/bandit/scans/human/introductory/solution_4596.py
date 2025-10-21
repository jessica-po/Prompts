n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    cnt = cnt | a[i]

j = 0
ans = 0
while 1:
    if (cnt >> j & 1 == 0):
        ans += 1
        j += 1
    else:
        break
print(ans)