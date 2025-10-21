lanes = []

for i in range(4):
    lanes.append(list(map(int, input().split())))

lanes.extend(lanes)

for i in range(4):
    ln = lanes[i]
    if (ln[3] and (ln[0] or ln[1] or ln[2])) or \
            (ln[0] and lanes[i + 3][3]) or \
            (ln[1] and lanes[i + 2][3]) or \
            (ln[2] and lanes[i + 1][3]):
        print('YES')
        break
else:
    print('NO')