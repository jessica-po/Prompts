n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 0
count = 1
i = 0
answer = []
while i < len(a) and s <= m:
    if a[i] == count:
        i += 1
        count += 1
    else:
        s += count
        answer.append(count)
        count += 1
if s > m:
    s = s - count + 1
    print(len(answer) - 1)
    for i in range(len(answer) - 1):
        print(answer[i], end = ' ')
elif s == m:
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end = ' ')
else:
    while s <= m:
        s += count
        answer.append(count)
        count += 1
    if s == m:
        print(len(answer))
        for i in range(len(answer)):
            print(answer[i], end = ' ')
    else:
        s = s - count + 1
        print(len(answer) - 1)
        for i in range(len(answer) - 1):
            print(answer[i], end = ' ')