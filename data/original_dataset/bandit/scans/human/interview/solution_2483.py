n, C = map(int, input().split())
time = 0
stc = []
for i in range(n):
    temp = list(map(int, input().split()))
    time = max(time, temp[1])
    stc.append(temp)
tv = [[0 for i in range(C)] for i in range(time + 1)]
for i in stc:
    s, t, c = i[0], i[1], i[2]
    for j in range(s, t + 1):
        tv[j][c - 1] = 1
ans = 0
for i in tv:
    ans = max(ans, sum(i))
print(ans)