f = []
for i in range(2):
    f.append(list(input()))


answer = 0

n = len(f[0])
for i in range(n):
    if f[0][i] == f[1][i] == '0' and i + 1 < n:
        if f[0][i + 1] == '0':
            answer += 1
            f[0][i + 1] = 'X'
        elif f[1][i + 1] == '0':
            answer += 1
            f[1][i + 1] = 'X'

    elif (f[1][i] == '0' or f[0][i] == '0') and i + 1 < n and f[0][i + 1] == f[1][i + 1] == '0':
        answer += 1
        f[0][i + 1] = f[1][i + 1] = 'X'


print(answer)