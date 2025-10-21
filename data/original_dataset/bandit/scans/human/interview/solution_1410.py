from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
cost = [list(map(int, input().split())) for i in range(3)]
info = [list(map(int, input().split())) for i in range(n-1)]
graph = [[] for i in range(n)]

for i in range(n-1):
    a, b = info[i]
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    if len(i) >= 3:
        print(-1)
        return

for i, j in enumerate(graph):
    if len(j) == 1:
        start = i
        break

visited = [-1]*n
visited[start] = 0
q = deque([start])

while q:
    pos = q.popleft()
    for next_pos in graph[pos]:
        if visited[next_pos] != -1:
            continue
        visited[next_pos] = (visited[pos] + 1) % 3
        q.append(next_pos)

ans = float("inf")
ind = [0, 1, 2]
for ptn in [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]:
    tmp_ans = 0
    for i in range(n):
        tmp_ans += cost[ptn[visited[i]]][i]
    if tmp_ans < ans:
        ans = tmp_ans
        ind = ptn[0:]

print(ans)
new_ans = [0]*n
for i in range(n):
    new_ans[i] = ind[visited[i]] + 1
print(*new_ans)