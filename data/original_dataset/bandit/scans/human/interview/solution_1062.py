n = int(input())
s = input()
t = input()

def ff(ch):
    return ord(ch) - ord('a')

def answer(a, b, sc):
    print(cans + sc)
    print(a+1, b+1)
    return

cans = 0
matrix = [[None] * 26 for i in range(26)]
for i in range(n):
    matrix[ff(s[i])][ff(t[i])] = i
    if s[i] != t[i]:
        cans += 1

for i in range(26):
    for j in range(i):
        if matrix[i][j] is not None and matrix[j][i] is not None:
            answer(matrix[i][j], matrix[j][i], -2)

for i in range(26):
    for h in range(26):
        if h == i:
            continue
        for v in range(26):
            if v == i:
                continue
            if matrix[h][i] is not None and matrix[i][v] is not None:
                answer(matrix[h][i], matrix[i][v], -1)

answer(-2, -2, 0)