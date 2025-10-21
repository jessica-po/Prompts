import sys
import math
def getAndParseInt(num=1):
    string = (sys.stdin.readline()).strip()
    if num==1:
        return int(string)
    else:
        return [int(part) for part in string.split()]

def getAndParseString(num=1,delim=" "):
    string = (sys.stdin.readline()).strip()
    if num==1:
        return string
    else:
        return [part for part in string.split(delim)]

n, m = getAndParseInt(2)
adj_list = [[] for i in range(n)]
edge_list = []
for i in range(m):
    u, v = getAndParseInt(2)
    edge_list.append((u,v))
    adj_list[u-1].append(v-1)

visited = set()
stack = []
finished_exploring = [False for i in range(n)]
edge_colors = {}
acyclic = True

for i in range(n):
    if i not in visited:
        stack.append((i,0))
    else:
        continue
    while stack:
        cur_vertex, neigh_index = stack.pop()
        if neigh_index == 0:
            visited.add(cur_vertex)

        if neigh_index == len(adj_list[cur_vertex]):
            finished_exploring[cur_vertex] = True
        else:
            stack.append((cur_vertex, neigh_index + 1))
            neighbor = adj_list[cur_vertex][neigh_index]
            if neighbor not in visited:
                stack.append((neighbor, 0))
                edge_colors[(cur_vertex+1,neighbor+1)]='1'
                visited.add(neighbor)
            elif neighbor in visited and not finished_exploring[neighbor]:
                edge_colors[(cur_vertex+1,neighbor+1)]='2'
                acyclic = False
            else:
                edge_colors[(cur_vertex+1,neighbor+1)]='1'

if acyclic:
    print(1)
    output_list = ["1" for i in range(m)]
else:
    print(2)
    output_list = []
    for edge in edge_list:
        output_list.append(edge_colors[edge])
print(" ".join(output_list))