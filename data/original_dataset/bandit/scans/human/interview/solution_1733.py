from collections import defaultdict
n, flower, bee = list(map(int, input().split()))
roads = {}
for _ in range(n-1):
    x, y = list(map(int, input().split()))
    if x not in roads:
        roads[x] = [y]
    else:
        roads[x].append(y)
    if y not in roads:
        roads[y] = [x]
    else:
        roads[y].append(x)
flowers = defaultdict(int)

def dfs(bee, flower):
    q = []
    visited = set()
    visited.add(flower)
    last = -1
    for y in roads[flower]:
        if y == bee:
            last = y
            continue
        q.append([y, y])
    while q:
        now = q.pop()
        visited.add(now[0])
        flowers[now[1]] += 1
        for y in roads[now[0]]:
            if y not in visited:
                if y == bee:
                    last = now[1]
                    continue
                q.append([y, now[1]])
    return last
rem = dfs(bee, flower)
flower_total = sum(flowers.values())+1
print(n*(n-1)-(flower_total - flowers[rem])*(n-(flower_total)))