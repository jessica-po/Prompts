n = int(input())
p = list(map(int, input().split()))

ls = []
visited = [False for _ in range(n)]
cnt = 0
for i in range(n):
    j = i
    cnt = 0
    while not visited[j]:
        visited[j] = True
        cnt += 1
        j = p[j] - 1
    if 0 < cnt:
        ls.append(cnt)

ls.sort()
if 1 < len(ls):
    ls[-2] += ls[-1]
    ls.pop()

print(sum([x**2 for x in ls]))