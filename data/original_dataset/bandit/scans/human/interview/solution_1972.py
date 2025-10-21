import sys
n = 500001
sqrt = int(0.75 * n**0.5)

data = [0]*(n)
ans = [[]]
out = []
for i in range(1, sqrt):
    ans.append([0]*i)
j = int(sys.stdin.readline())
qus = sys.stdin.readlines()
for qu in qus:
    q = [int(i) for i in qu.split()]
    if q[0] == 1:
        x = q[1]
        y = q[2]
        data[x] += y
        for i in range(1, sqrt):
            ans[i][x%i] += y
    else:
        if q[1] < sqrt:
            out.append(str(ans[q[1]][q[2]]))
        else:
            out.append(str(sum([data[i] for i in range(q[2], n, q[1])])))
            
sys.stdout.write('\n'.join(out) + '\n')