from collections import deque

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]
link = [[] for _ in range(N)]

for i in range(M):
    link[L[i][0]-1].append(L[i][1]-1)
    link[L[i][1]-1].append(L[i][0]-1)

checked = [-1 for _ in range(N)]
checked[0] = 0
d = deque([0])
while d:
    now = d.popleft()
    for i in range(len(link[now])):
        if checked[link[now][i]] == -1:
            checked[link[now][i]] = now + 1
            d.append(link[now][i])


flag = False
for i in range(1, N):
    if checked[i] == -1:
        flag = True
        break

if flag:
    print('No')
else:
    print('Yes')
    for i in range(1, N):
        print(checked[i])