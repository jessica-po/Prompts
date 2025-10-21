import sys

fin = sys.stdin
fout = sys.stdout

a = [0] * 6
for i in range(6):
    a[i] = [0] * 6
for i in range(2):
    a[i][0] = 3
    a[i][1] = 3
    a[i][2] = 4
    a[i][3] = 4
    a[i][4] = 3
    a[i][5] = 3
for i in range(2, 4):
    a[i][0] = 2
    a[i][1] = 2
    a[i][2] = 3
    a[i][3] = 3
    a[i][4] = 2
    a[i][5] = 2
for i in range(4, 6):
    a[i][0] = 1
    a[i][1] = 1
    a[i][2] = 2
    a[i][3] = 2
    a[i][4] = 1
    a[i][5] = 1

ansI = -1
ansJ = -1

max = -1

ansL = []

for i in range(6):
    s = fin.readline().strip()
    ansL.append(s)
    s = s.replace("-", "")
    for j in range(6):
        if s[j] == '.' and a[i][j] > max:
            max = a[i][j]
            ansI = i
            ansJ = j

# print(ansI, ansJ)
for i in range(len(ansL)):
    cur = ansL[i]
    realJ = -1
    for j in range(len(cur)):
        if (cur[j] != '-'):
            realJ += 1
        if i == ansI and realJ == ansJ and cur[j] != '-':
            fout.write('P')
        else:
            fout.write(cur[j])

    fout.write("\n")
fin.close()
fout.close()