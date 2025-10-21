def LIHW(h):
    return [list(map(int, input().split())) for _ in range(h)]


N = int(input())
X = LIHW(N-1)

for i in range(N-1):
    time = [0]*N
    time[i] = X[i][1]+X[i][0]
    for j in range(i+1, N-1):
        if time[j-1] <= X[j][1]:
            time[j] = X[j][1]+X[j][0]
        else:
            if (time[j-1]-X[j][1]) % X[j][2] == 0:
                time[j] = time[j-1] + X[j][0]
            else:
                time[j] = time[j-1] + X[j][0]+X[j][2] - \
                    ((time[j-1]-X[j][1]) % X[j][2])
    print(time[j])
print(0)