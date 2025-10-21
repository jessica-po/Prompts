from collections import defaultdict
N, M = list(map(int, input().split()))

d = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)


def dfs(n, path):
    count = 0
    path.append(n)
    if len(path) == N:
        count += 1
        return count
    for i in d[n]:
        if i not in path:
            count += dfs(i, path)
            path.pop()

    return count


print((dfs(1, [])))