N = int(input())
u, v, w = [0]*(N-1), [0]*(N-1), [0]*(N-1)
n = [-1] * N
# n[][0] 色　n[][1] 連結先一覧リスト n[][2] mod2 
for i in range(N):
    n[i] = [0]*4
    n[i][1] = []
    n[i][2] = []

for i in range(N-1):
    u[i], v[i], w[i] = list(map(int, input().split()))
    n[u[i]-1][1].append(v[i]-1)
    n[v[i]-1][1].append(u[i]-1)
    n[u[i]-1][2].append(w[i]%2)
    n[v[i]-1][2].append(w[i]%2)

stack = [u[0]-1]

while True:
    num = stack.pop()
    n[num][3] = 1
    for i in range(len(n[num][1])):
        if n[n[num][1][i]][3] == 0:
            stack.append(n[num][1][i])
            if n[num][2][i] == 0:
                n[n[num][1][i]][0] = n[num][0]
            else:
                n[n[num][1][i]][0] = -1 * n[num][0] + 1
    if len(stack) == 0:
        break

for i in n:
    print(i[0])