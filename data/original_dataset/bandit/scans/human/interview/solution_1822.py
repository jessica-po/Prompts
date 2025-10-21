n, x = list(map(int, input().split()))
link1 = list(map(int, input().split()))
link2 = [0] * (n + 1)
for i, v in enumerate(link1, 1):
    if v != 0:
        link2[v] = i


table = [False] * n
table[0] = True
for i, v in enumerate(link1, 1):
    if v == 0:
        len = 0
        flag = False
        now = i
        while now:
            len += 1
            if now == x:
                flag = True
                pos = len
            now = link2[now]
        if not flag:
            for j in reversed(list(range(n - len))):
                if table[j]:
                    table[j + len] = True
for i in range(n):
    if table[i]:
        print(i + pos)