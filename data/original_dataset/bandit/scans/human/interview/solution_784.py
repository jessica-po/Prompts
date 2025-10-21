3

prev = dict()

def dfs(a, b):
    if a > b:
        return
    if 2 * a not in prev:
        prev[2 * a] = a
        dfs(2 * a, b)
    if 10 * a + 1 not in prev:
        prev[10 * a + 1] = a
        dfs(10 * a + 1, b)



a, b = list(map(int, input().split()))
dfs(a, b)

if b not in prev:
    print("NO")
else:
    print("YES")
    path = []
    while b != a:
        path.append(b)
        b = prev[b]
    path.append(a)
    path.reverse()
    print(len(path))
    print(*path)