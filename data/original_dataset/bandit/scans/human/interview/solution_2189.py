#!/usr/local/bin/python3

from collections import defaultdict
import heapq

num_nodes, num_edges = list(map(int, input().split()))

ins = defaultdict(set)
out = defaultdict(int)

for _ in range(num_edges):
    node_out, node_in = list(map(int, input().split()))
    ins[node_in].add(node_out)
    out[node_out] += 1

zeros = [-node for node in range(num_nodes, 0, -1) if out[node] == 0]

final_mappings = {}
current_index = num_nodes

while current_index > 0:

    node = -heapq.heappop(zeros)
    final_mappings[node] = current_index
    current_index -= 1

    for node_out in ins[node]:
        out[node_out] -= 1
        if out[node_out] == 0:
            heapq.heappush(zeros, -node_out)
    
print(' '.join(str(final_mappings[node]) for node in range(1, num_nodes + 1)))