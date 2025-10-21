3

s = input()
n = len(s)

a, b = 0, 0
d = dict()
for i in range(len(s)):
    if s[i] in d:
        a = d[s[i]]
        b = i
    d[s[i]] = i

if a == b - 1:
    print("Impossible")
else:
    ans = [[' '] * 13 for i in range(2)]
    if (b - a) % 2 == 1:
        for i in range((b - a) // 2):
            ans[0][-(b - a) // 2 + i + 1] = s[a + i + 1]
            ans[1][-i - 1] = s[a + i + (b - a) // 2 + 1]
        x = -(b - a) // 2
        y = 0
        for i in range(b, n):
            ans[y][x] = s[i]
            if y == 0:
                x -= 1
            else:
                x += 1
            if x == -14:
                y = 1
                x = 0
        for i in range(a):
            ans[y][x] = s[i]
            if y == 0:
                x -= 1
            else:
                x += 1
            if x == -14:
                y = 1
                x = 0
        print("".join(ans[0]))
        print("".join(ans[1]))
    else:
        for i in range((b - a) // 2):
            ans[0][-(b - a) // 2 + i + 1] = s[a + i + 1]
            ans[1][-i - 1] = s[a + i + (b - a) // 2]
        x = -(b - a) // 2
        y = 0
        for i in range(b, n):
            ans[y][x] = s[i]
            if y == 0:
                x -= 1
            else:
                x += 1
            if x == -14:
                y = 1
                x = 0
        for i in range(a):
            ans[y][x] = s[i]
            if y == 0:
                x -= 1
            else:
                x += 1
            if x == -14:
                y = 1
                x = 0
        print("".join(ans[0]))
        print("".join(ans[1]))