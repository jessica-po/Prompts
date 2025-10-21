class Edge:
    def __init__(self, to, cost, capacity, next_edge):
        self.to = to
        self.cost = cost
        self.origin_cost = cost
        self.capacity = capacity
        self.next_edge = next_edge
        self.pair = None


class MinCostMaxFlow:
    def __init__(self, max_node):
        self.null = Edge(0, 0, 0, None)
        self.max_node = max_node + 3
        self.total_cost = 0
        self.current_cost = 0
        self.visited = [False] * self.max_node
        self.arc_list = []
        self.edge_head = [self.null] * self.max_node
        self.source = max_node + 1
        self.sink = max_node + 2

    def AddArcWithCapacityAndUnitCost(self, start_node, end_node, capacity, cost):
        self.edge_head[start_node] = Edge(end_node, cost, capacity, self.edge_head[start_node])
        self.edge_head[end_node] = Edge(start_node, -cost, 0, self.edge_head[end_node])
        self.edge_head[start_node].pair = self.edge_head[end_node]
        self.edge_head[end_node].pair = self.edge_head[start_node]
        if start_node != self.source and start_node != self.sink and end_node != self.source and end_node != self.sink:
            self.arc_list.append(self.edge_head[end_node])

    def NumArcs(self):
        return len(self.arc_list)

    def Tail(self, index):
        return self.arc_list[index].to

    def Head(self, index):
        return self.arc_list[index].pair.to

    def UnitCost(self, index):
        return self.arc_list[index].pair.origin_cost

    def Flow(self, index):
        return self.arc_list[index].capacity

    def OptimalFlow(self):
        edge = self.edge_head[self.sink]
        total_flow = 0
        while id(edge) != id(self.null):
            total_flow += edge.capacity
            edge = edge.next_edge
        return total_flow

    def OptimalCost(self):
        return self.total_cost

    def SetNodeSupply(self, node, supply):
        if supply > 0:
            self.AddArcWithCapacityAndUnitCost(self.source, node, supply, 0)
        elif supply < 0:
            self.AddArcWithCapacityAndUnitCost(node, self.sink, -supply, 0)

    def aug(self, node_id, total_flow):
        if node_id == self.sink:
            self.total_cost += self.current_cost * total_flow
            return total_flow
        self.visited[node_id] = True
        flow = total_flow
        edge = self.edge_head[node_id]
        while id(edge) != id(self.null):
            if edge.capacity > 0 and edge.cost == 0 and not self.visited[edge.to]:
                delta = self.aug(edge.to, min(flow, edge.capacity))
                edge.capacity -= delta
                edge.pair.capacity += delta
                flow -= delta
                if flow == 0:
                    return total_flow
            edge = edge.next_edge
        return total_flow - flow

    def modify_label(self):
        min_cost = 1 << 63
        for node_id in range(0, self.max_node):
            if not self.visited[node_id]:
                continue
            edge = self.edge_head[node_id]
            while id(edge) != id(self.null):
                if edge.capacity > 0 and not self.visited[edge.to] and edge.cost < min_cost:
                    min_cost = edge.cost
                edge = edge.next_edge
        if min_cost == 1 << 63:
            return False
        for node_id in range(0, self.max_node):
            if not self.visited[node_id]:
                continue
            edge = self.edge_head[node_id]
            while id(edge) != id(self.null):
                edge.cost -= min_cost
                edge.pair.cost += min_cost
                edge = edge.next_edge
        self.current_cost += min_cost
        return True

    def Solve(self):
        while True:
            while True:
                self.visited = [False] * self.max_node
                if self.aug(self.source, 1 << 63) == 0:
                    break
            if not self.modify_label():
                break
        return self.total_cost


def main():
    s = input()
    n = int(input())
    source = 0
    sink = n + 26 + 1
    mcmf = MinCostMaxFlow(n + 28)
    length = len(s)
    num = [0] * 29
    for i in range(0, length):
        num[ord(s[i]) - ord('a') + 1] += 1
    for i in range(1, 27):
        if num[i] > 0:
            mcmf.AddArcWithCapacityAndUnitCost(i, sink, num[i], 0)
    for i in range(1, n + 1):
        s, used = input().split(' ')
        mcmf.AddArcWithCapacityAndUnitCost(source, 26 + i, int(used), 0)
        num = [0] * 29
        for j in range(0, len(s)):
            num[ord(s[j]) - ord('a') + 1] += 1
        for j in range(1, 27):
            if num[j] > 0:
                mcmf.AddArcWithCapacityAndUnitCost(26 + i, j, num[j], i)
    mcmf.SetNodeSupply(source, 1 << 63)
    mcmf.SetNodeSupply(sink, -(1 << 63))
    mcmf.Solve()
    if mcmf.OptimalFlow() != length:
        print("-1")
    else:
        print(mcmf.OptimalCost())


def __starting_point():
    main()

__starting_point()