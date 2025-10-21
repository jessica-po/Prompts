num = list(map(int, input()))
best = num[:]
for i in range(-1, -len(num) - 1, -1):
    if num[i] == 0:
        continue
    num[i] -= 1
    for j in range(i + 1, 0):
        num[j] = 9
    if sum(num) > sum(best):
        best = num[:]
s = ''.join(map(str, best)).lstrip('0')
print(s)