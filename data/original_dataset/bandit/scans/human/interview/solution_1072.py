line = input().split()
n = int(line[0])
m = int(line[1])

lst = [input()]
sml = []
for i in range(n - 1):
    lst.append(input())
    sml.append(False)

ans = 0
for i in range(m):
    flag = True
    for j in range(n - 1):
        flag = flag and ((lst[j][i] <= lst[j + 1][i]) or sml[j])
    if flag:
        for j in range(n - 1):
            if lst[j][i] < lst[j + 1][i]:
                sml[j] = True
    else:
        ans += 1

print(str(ans))