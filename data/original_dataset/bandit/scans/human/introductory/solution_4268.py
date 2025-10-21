import math
n , d = list(map(int, input().split()))

x = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
sum_tmp = 0

for i in range(n):
    for j in range(i+1, n):
        for h in range(d):
            sum_tmp += (x[i][h] - x[j][h]) ** 2
        if math.sqrt(sum_tmp).is_integer():
            cnt += 1
        sum_tmp = 0

print(cnt)