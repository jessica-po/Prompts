read = lambda: list(map(int, input().split()))
n, c = read()
t = list(read())
cnt = 1
for i in range(1, n):
    if t[i] - t[i - 1] > c:
        cnt = 1
    else:
        cnt += 1
print(cnt)