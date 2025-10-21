n = int(input())
a = list(map(int, input().split()))
res = 0
new_a = []
for i in range(n):
    if a[i] % 2 == 0:
        if a[i] > 0:
            res += a[i]
    else:
        new_a.append(a[i])
a = new_a
a.sort()
res += a[-1]
a.pop()
while len(a) > 1:
    if a[-1] + a[-2] > 0:
        res += a[-1] + a[-2]
        a.pop()
        a.pop()
    else:
        break
print(res)