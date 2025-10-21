n = int(input())
s = input()
x = 0
y = 0
ans = 0
pred = -1
for c in s:
    if c == 'U':
        y += 1
    else:
        x += 1
    if x == y:
        continue
    if x > y:
        cur = 0
    else:
        cur = 1
    if cur != pred and pred != -1:
        ans += 1
    pred = cur
print(ans)