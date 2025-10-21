import sys
from collections import defaultdict

class MaxFlow(object):
    def __init__(self):
        self.edges = defaultdict(lambda: defaultdict(lambda: 0))

    def add_edge(self, u, v, capacity=float('inf')):
        self.edges[u][v] = capacity

    def bfs(self, s, t):
        open_q = [s]

        visited = set()
        parent = dict()
        while open_q:
            close_q = []
            for node in open_q:
                for v, capacity in list(self.edges[node].items()):
                    if v not in visited and capacity > 0:
                        close_q.append(v)
                        parent[v] = node
                        visited.add(v)
                        if v == t:
                            result = []
                            n2 = v
                            n1 = node
                            while n1 != s:
                                result.append((n1, n2))
                                n2 = n1
                                n1 = parent[n1]
                            result.append((n1, n2))
                            return result

            open_q = close_q

        return None

    def solve(self, s, t):
        flow = 0
        route = self.bfs(s, t)
        while route is not None:
            new_flow = float('inf')
            for _, (n1, n2) in enumerate(route):
                new_flow = min(new_flow, self.edges[n1][n2])
            for _, (n1, n2) in enumerate(route):
                self.edges[n1][n2] -= new_flow
                self.edges[n2][n1] += new_flow
            flow += new_flow

            route = self.bfs(s, t)

        return flow

    def __str__(self):
        result = "{ "
        for k, v in list(self.edges.items()):
            result += str(k) + ":" + str(dict(v)) + ", "
        result += "}"
        return result


def main():
    (n, m) = tuple([int(x) for x in input().split()])
    r = []
    xs = set()
    ys = set()
    for i in range(m):
        (x1, y1, x2, y2) = tuple(int(x) for x in input().split())
        r.append((x1, y1, x2, y2))
        xs.add(x1)
        xs.add(x2 + 1)
        ys.add(y1)
        ys.add(y2 + 1)

    xx = sorted(xs)
    yy = sorted(ys)
    xsize = len(xs)
    ysize = len(ys)
    grid = []
    for i in range(ysize):
        grid.append([False] * xsize)

    for rect in r:
        x1 = rect[0]
        y1 = rect[1]
        x2 = rect[2]
        y2 = rect[3]
        for i, y in enumerate(yy):
            for j, x in enumerate(xx):
                if x1 <= x and y1 <= y and x2 >= x and y2 >= y:
                    grid[i][j] = True

    f = MaxFlow()
    for i in range(len(yy)):
        for j in range(len(xx)):
            if grid[i][j]:
                f.add_edge(1 + i, len(yy) + 1 + j, float('inf'))
    for i in range(len(yy) - 1):
        f.add_edge(0, i + 1, yy[i + 1] - yy[i])
    for i in range(len(xx) - 1):
        f.add_edge(len(yy) + 1 + i, len(xx) + len(yy) + 1, xx[i + 1] - xx[i])

    # print(xx)
    # print(yy)
    # print(f)
    print(f.solve(0, len(xx) + len(yy) + 1))


def __starting_point():
    main()

__starting_point()