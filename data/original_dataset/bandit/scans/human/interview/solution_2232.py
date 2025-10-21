import sys

n = int(sys.stdin.readline())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    i, j = tuple(int(k) for k in sys.stdin.readline().split())
    i -= 1
    j -= 1
    edges[i].append(j)
    edges[j].append(i)

# Prunes the graph starting from the vertices with
# only 1 edge until we reach a vertex with 3+ edges.
# Stores the distance from each non-pruned vertex
# to each of the leaves it reaches.
def prune():
    pruned = [False for _ in range(n)]
    leaves = [[] for _ in range(n)]
    todo = []
    for i in range(n):
        if len(edges[i]) == 1:
            todo.append((0, i, i))
    while len(todo) > 0:
        d, i, j = todo.pop()
        pruned[j] = True
        for k in edges[j]:
            if not pruned[k]:
                if len(edges[k]) < 3:
                    todo.append((d + 1, i, k))
                else:
                    leaves[k].append((d + 1, i))
    return pruned, leaves

pruned, leaves = prune()

# Returns the furthest non-pruned vertices
# from another non-pruned vertex.
def furthest(i):
    assert not pruned[i]
    visited = list(pruned)
    top_distance = 0
    top_vertices = [i]
    todo = [(0, i)]
    while len(todo) > 0:
        d, i = todo.pop()
        visited[i] = True
        if d > top_distance:
            top_distance = d
            top_vertices = []
        if d == top_distance:
            top_vertices.append(i)
        for j in edges[i]:
            if not visited[j]:
                todo.append((d + 1, j))
    return top_distance, top_vertices

# Single center topology.
# Only 1 vertex with 3+ edges.
def solve_single_center(i):
    l = list(reversed(sorted(leaves[i])))[:4]
    return list(l[j][1] for j in range(4))

# Scores non-pruned vertices according to the sum
# of the distances to their two furthest leaves.
def vertices_score(v):
    scores = []
    for i in v:
        assert not pruned[i]
        l = list(reversed(sorted(leaves[i])))[:2]
        score = (l[0][0] + l[1][0]), l[0][1], l[1][1]
        scores.append(score)
    return list(reversed(sorted(scores)))

# Single cluster topology.
# 1 cluster of vertices, all equally far away from each other.
def solve_single_cluster(v):
    scores = vertices_score(v)[:2]
    return scores[0][1], scores[1][1], scores[0][2], scores[1][2]

# Double cluster topology.
# 2 clusters of vertices, pairwise equally far away from each other.
def solve_double_cluster(v1, v2):
    scores1 = vertices_score(v1)[:1]
    scores2 = vertices_score(v2)[:1]
    return scores1[0][1], scores2[0][1], scores1[0][2], scores2[0][2]

def solve():
    def start_vertex():
        for i in range(n):
            if not pruned[i]:
                return i
    i = start_vertex()
    distance, v1 = furthest(i)
    if distance == 0:
        return solve_single_center(v1[0])
    else:
        distance, v1 = furthest(v1[0])
        distance, v2 = furthest(v1[0])
        v = list(set(v1) | set(v2))
        if len(v) < len(v1) + len(v2):
            return solve_single_cluster(v)
        else:
            return solve_double_cluster(v1, v2)

a, b, c, d = solve()
print(a + 1, b + 1)
print(c + 1, d + 1)