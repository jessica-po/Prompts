n, m, p = list(map(int, input().split()))
speeds = list(map(int, input().split()))

field = []
for _ in range(n):
    s = list(input().strip())
    field.append(s)


def neighbours(i, j):
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= i+di < n and 0 <= j+dj < m:
            yield i+di, j+dj

def colors():
    return [str(i) for i in range(1, p+1)]


edges = {c:[] for c in colors()}
for c in colors():
    for i in range(n):
        for j in range(m):
            if field[i][j] == c:
                if not all(field[n_i][n_j] == c for (n_i, n_j) in neighbours(i, j)):
                    edges[c].append((i,j))
# print(edges)


def up_field(color):
    edge_color = edges[color]

    new_edge = []
    for (i,j) in edge_color:
        for (n_i, n_j) in neighbours(i, j):
            if field[n_i][n_j] == '.':
                field[n_i][n_j] = color
                new_edge.append((n_i, n_j))
    edges[color] = new_edge


def print_field():
    for l in field:
        print(l)
    print('-'*100)

# print_field()


while any(len(x) > 0 for x in list(edges.values())):
    for s, c in zip(speeds, colors()):
        for i in range(s):
            up_field(c)
            if len(edges[c]) == 0:
                break

    # print_field()


counts = {c:0 for c in colors()}
counts['.'] = 0
counts['#'] = 0

for i in range(n):
    for j in range(m):
        counts[field[i][j]] += 1

print(*(counts[c] for c in colors()))