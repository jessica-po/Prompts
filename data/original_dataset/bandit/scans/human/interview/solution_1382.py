def read_data():
    n, m = list(map(int, input().split()))
    Es = [[] for v in range(n)]
    for e in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        Es[a].append(b)
        Es[b].append(a)
    return n, m, Es

def solve(n, m, Es):
    if m == 0:
        return 3, n * (n - 1) * (n - 2) // 6
    if max(list(map(len, Es))) == 1:
        return 2, m * (n-2)
    patterns = 0
    color = [0] * n
    for u in range(n):
        if color[u]:
            continue
        color[u] = 1
        stack = [u]
        n_color = [1, 0]
        while stack:
            v = stack.pop()
            prev_color = color[v]
            for w in Es[v]:
                current_color = color[w]
                if current_color == prev_color:
                    return 0, 1
                if current_color == 0:
                    color[w] = - prev_color
                    n_color[(prev_color + 1)//2] += 1
                    stack.append(w)
        n_even = n_color[0]
        n_odd = n_color[1]
        patterns += n_even * (n_even - 1) // 2 + n_odd * (n_odd - 1) // 2
    return 1, patterns

def __starting_point():
    n, m, Es = read_data()
    print(*solve(n, m, Es))

__starting_point()