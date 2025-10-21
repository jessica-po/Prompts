h, w = list(map(int, input().split()))
A = []

for i in range(h):
    line = list(map(int, input().split()))
    A.append(line)

for i in range(h):
    line = list(map(int, input().split()))
    for j, num in enumerate(line):
        A[i][j] = abs(A[i][j] - num)

const = 6400
mask = 1 << const
DP = [0]*w
DP[0] = mask >> A[0][0]


def slide_down(y, x):
    bit = DP[x]
    delta = A[y+1][x]
    new1 = bit << delta
    new2 = bit >> delta
    DP[x] = new1 | new2


def slide_right(y, x):
    bit = DP[x]
    delta = A[y][x+1]
    new1 = bit << delta
    new2 = bit >> delta
    DP[x+1] |= new1 | new2


for y in range(h):
    for x in range(w):
        if x < w-1:
            slide_right(y, x)
        if y < h-1:
            slide_down(y, x)

pattern = DP[w-1]
for i in range(81):
    if (pattern >> const+i) & 1 or (pattern >> const-i) & 1:
        print(i)
        return