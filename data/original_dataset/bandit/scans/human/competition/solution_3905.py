import sys

# sys.stind.readline lee datos el doble de
# rápido que la funcion por defecto input
input = sys.stdin.readline
length = len


def get_input():
    n, m, h = [int(x) for x in input().split(' ')]

    digraph = [[] for _ in range(n + 1)]
    transpose = [[] for _ in range(n + 1)]
    mantainence = [0] + [int(x) for x in input().split(' ')]

    for _ in range(m):
        c1, c2 = [int(x) for x in input().split(' ')]

        if (mantainence[c1] + 1) % h == mantainence[c2]:
            digraph[c1].append(c2)
            transpose[c2].append(c1)
        if (mantainence[c2] + 1) % h == mantainence[c1]:
            digraph[c2].append(c1)
            transpose[c1].append(c2)

    return digraph, transpose


def dfs_cc_1_visit(graph, node, color, finalization_stack):
    stack = [node]

    while stack:
        current_node = stack[-1]

        if color[current_node] != 'white':
            stack.pop()
            if color[current_node] == 'grey':
                finalization_stack.append(current_node)
                color[current_node] = 'black'
            continue

        color[current_node] = 'grey'
        for adj in graph[current_node]:
            if color[adj] == 'white':
                stack.append(adj)


def dfs_cc_1(graph):
    n = length(graph)
    finalization_stack = []
    color = ['white'] * n
    for i in range(1, n):
        if color[i] == 'white':
            dfs_cc_1_visit(graph, i, color, finalization_stack)    
    return finalization_stack


def dfs_cc_2_visit(graph, node, color, scc, component):
    stack = [node]

    while stack:
        current_node = stack[-1]

        if color[current_node] != 'white':
            stack.pop()
            color[current_node] = 'black'
            scc[current_node] = component
            continue

        color[current_node] = 'grey'
        for adj in graph[current_node]:
            if color[adj] == 'white':
                stack.append(adj)


def dfs_cc_2(graph, stack_time):
    n = length(graph)
    color = ['white'] * n
    scc = [0] * n
    component = 0
    while stack_time:
        current_node = stack_time.pop()
        if color[current_node] == 'white':
            dfs_cc_2_visit(graph, current_node, color, scc, component)
            component += 1

    return scc, component


def strongly_connected_components(digraph, transpose):
    stack_time = dfs_cc_1(digraph)
    scc, max_component = dfs_cc_2(transpose, stack_time)

    # create the components
    out_deg = [0] * max_component
    scc_nodes = [[] for _ in range(max_component)]
    for node in range(1, length(digraph)):
        scc_nodes[scc[node]].append(node)
        for adj in digraph[node]:
            if scc[node] != scc[adj]:
                out_deg[scc[node]] += 1
    
    # searching minimum strongly connectected component with out degree 0
    minimum_component = None
    for i, value in enumerate(out_deg):
        if value == 0 and (minimum_component is None or length(scc_nodes[i]) < length(scc_nodes[minimum_component])):
            minimum_component = i
    
    # return the size of the component and the nodes
    return length(scc_nodes[minimum_component]), scc_nodes[minimum_component]


def __starting_point():
    digraph, transpose = get_input()
    count, nodes = strongly_connected_components(digraph, transpose)
    
    print(count)
    print(' '.join([str(x) for x in nodes]))

__starting_point()