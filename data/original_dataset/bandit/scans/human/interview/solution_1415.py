a, b, x, y = map(int, input().split())
s = input()
p = []
for i in range(a + 1):
    p.append([0] * (b + 1))
sum = 0
for i in range(len(s)):
    if p[x][y] == 0:
        p[x][y] = 1
        print(1, end = ' ')
        sum += 1
    else:
        print(0, end = ' ')
    if s[i] == 'U' and x != 1:
        x -= 1
    if s[i] == 'D' and x != a:
        x += 1
    if s[i] == 'L' and y != 1:
        y -= 1
    if s[i] == 'R' and y != b:
        y += 1
print(a * b - sum)