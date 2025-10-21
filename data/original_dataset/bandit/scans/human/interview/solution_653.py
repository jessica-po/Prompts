n = int(input())
s = input()

num = '0123456789'
state = [0]*(10)
for i in s:
    if i in num:
        state[int(i)] = 0
    else:
        if i=='L':
            for j in range(10):
                if state[j]==0:
                    state[j] = 1
                    break
        else:
            for j in range(9, -1, -1):
                if state[j] == 0:
                    state[j] = 1
                    break

for i in state:
    print(i, end='')