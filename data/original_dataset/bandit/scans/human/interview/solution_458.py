a, b, c = list(map(int, input().split()))
ans = []
for sum in range(1, 200):
    x = b * sum ** a + c
    if x <= 0 or x >= 10 ** 9:
        continue
    summ = 0
    for aa in str(x):
        summ += int(aa)
    if sum == summ:
        ans.append(x)
print(len(ans))
print(*ans)