from collections import deque
 
 
class Dinic:
    def __init__(self, n: int):
        """頂点数をnとする"""
        self.INF = float("inf")
        self.n = n
        self.graph = [[] for _ in range(n)]
 
    def add_edge(self, _from: int, to: int, capacity: int):
        """残余グラフを構築
        1. _fromからtoへ向かう容量capacityの辺をグラフに追加する
        2. toから_fromへ向かう容量0の辺をグラフに追加する
        """
        forward = [to, capacity, None]
        forward[2] = backward = [_from, 0, forward]
        self.graph[_from].append(forward)
        self.graph[to].append(backward)
 
    def bfs(self, s: int, t: int):
        """capacityが正の辺のみを通ってsからtに移動可能かどうかBFSで探索
        level: sからの最短路の長さ
        """
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            _from = q.popleft()
            for to, capacity, _ in self.graph[_from]:
                if capacity > 0 and self.level[to] < 0:
                    self.level[to] = self.level[_from] + 1
                    q.append(to)
 
    def dfs(self, _from: int, t: int, f: int) -> int:
        """流量が増加するパスをDFSで探索
        BFSによって作られた最短路に従ってfを更新する
        """
        if _from == t:
            return f
        for edge in self.itr[_from]:
            to, capacity, reverse_edge = edge
            if capacity > 0 and self.level[_from] < self.level[to]:
                d = self.dfs(to, t, min(f, capacity))
                if d > 0:
                    edge[1] -= d
                    reverse_edge[1] += d
                    return d
        return 0
 
    def max_flow(self, s: int, t: int):
        """s-tパス上の最大流を求める
        計算量: O(|E||V|^2)
        """
        flow = 0
        while True:
            self.bfs(s, t)
            if self.level[t] < 0:
                break
            self.itr = list(map(iter, self.graph))
            f = self.dfs(s, t, self.INF)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.INF)
        return flow

n = int(input())
a = list(map(int, input().split()))

dinic = Dinic(n + 2)
s = 0
t = n + 1
_sum = 0
for i in range(0, n):
    if a[i] > 0:
        dinic.add_edge(s, i+1, 0)
        dinic.add_edge(i+1, t, a[i])
        _sum += a[i]
    elif a[i] < 0:
        dinic.add_edge(s, i+1, -a[i])
        dinic.add_edge(i+1, t, 0)
    else:
        dinic.add_edge(s, i+1, 0)
        dinic.add_edge(i+1, t, 0)

for i in range(n):
    num = i+1
    next_num = 2 * num
    while next_num <= n:
        dinic.add_edge(num, next_num, 10**18)
        next_num += num

print(_sum - dinic.max_flow(s, t))