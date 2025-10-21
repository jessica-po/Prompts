from itertools import chain
import numpy as np
import networkx as nx

h, w, *X = map(int, open(0).read().split())
C = np.array(X[:100], dtype=int).reshape((10, 10))
A = np.array(X[100:], dtype=int).reshape((h, w))

G = nx.DiGraph(C)
d = {-1:0}
for i in range(10):
    d[i] = nx.shortest_path_length(G, i, 1, weight='weight')
print(sum(d[a] for a in chain.from_iterable(A)))