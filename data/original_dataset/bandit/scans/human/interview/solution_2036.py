n, m, sx, sy = list(map(int, input().split()))

print(sx, sy)

# its row
for j in range(1, m+1):
    if j != sy:
        print(sx, j)

# other rows
curr = m
for i in range(1, n+1):
    if i != sx:
        if curr == m:
            for j in range(m, 0, -1):
                print(i, j)
                curr = 0
        else:
            for j in range(1, m+1):
                print(i, j)
                curr = m