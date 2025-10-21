#python3
# utf-8

nodes_nr, edges_nr = (int(x) for x in input().split())
node_idx___cost = [int(x) for x in input().split()]
node_idx___neigh_idxes = [[] for x in range(nodes_nr)]
for _ in range(edges_nr):
    node1_idx, node2_idx = (int(x) - 1 for x in input().split())
    node_idx___neigh_idxes[node1_idx].append(node2_idx)
    node_idx___neigh_idxes[node2_idx].append(node1_idx)

node_idx___is_visited = [False for x in range(nodes_nr)]

ans = 0
for node_idx in range(nodes_nr):
    if node_idx___is_visited[node_idx]:
        continue
    stack = [node_idx]
    node_idx___is_visited[node_idx] = True
    cheapest_cost = node_idx___cost[node_idx]
    while stack:
        curr_node_idx = stack.pop()
        for neigh_idx in node_idx___neigh_idxes[curr_node_idx]:
            if node_idx___is_visited[neigh_idx]:
                continue
            stack.append(neigh_idx)
            cheapest_cost = min(cheapest_cost, node_idx___cost[neigh_idx])
            node_idx___is_visited[neigh_idx] = True
    ans += cheapest_cost
print(ans)