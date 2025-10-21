n = int(input())
a = list(map(int, input().split()))
cnt, good = 0, 0
for i in range(0, n):
    if a[i] == 4 or a[i] == 5:
        good = good + 1
    else:
        good = 0
    if good == 3:
        cnt = cnt + 1
        good = 0
print(cnt)