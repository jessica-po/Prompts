n = int(input())
bs = []
for _ in range(n):
    bs.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(n):
        if i != j and bs[i][0] == bs[j][1]:
            ans += 1
            break

print(n - ans)