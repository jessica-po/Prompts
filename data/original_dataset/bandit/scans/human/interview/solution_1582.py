N = int(input())
keep = [[0 for i in range(10)] for j in range(10)]
ans = 0

for i in range(1, N + 1):
    first = int(str(i)[0])
    end = int(str(i)[-1])
    keep[first - 1][end - 1] += 1

for i in range(9):
    for j in range(9):
        ans += (keep[i][j] * keep[j][i])
print(ans)