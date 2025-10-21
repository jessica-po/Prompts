r, c = list(map(int, input().split()))
cake = [input().strip() for _ in range(r)]
ans = 0
for i in range(r):
    for j in range(c):
        if cake[i][j] == '.' and ('S' not in cake[i] or 'S' not in list(zip(*cake))[j]):
            ans += 1
print(ans)