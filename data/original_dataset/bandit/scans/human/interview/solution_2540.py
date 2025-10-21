from collections import defaultdict


class SumDefaultdict(defaultdict):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(int, *args, **kwargs)
        self.mx = max(self.values())
        self.mx_sum = sum(c for c, v in list(self.items()) if v == self.mx)

    def sumadd(self, map):
        for bb, val in list(map.items()):
            if val > 0:
                self[bb] += val
                if self[bb] > self.mx:
                    self.mx = self[bb]
                    self.mx_sum = bb
                elif self[bb] == self.mx:
                    self.mx_sum += bb

def go():
    n = int(input())
    c = list(map(int, input().split()))

    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = [int(x) - 1 for x in input().split()]
        edges[a].append(b)
        edges[b].append(a)

    depth = [0] + [None] * (n - 1)
    parent = [None] * n
    que = [0]
    index = 0
    while index < len(que):
        curr = que[index]
        for b in edges[curr]:
            if depth[b] is None:
                depth[b] = depth[curr] + 1
                parent[b] = curr
                que.append(b)
        index += 1

    order = sorted(((depth[i], i) for i in range(n)), reverse=True)

    cols = [SumDefaultdict({c[i]: 1}) for i in range(n)]
    answer = [0] * n
    for d, i in order:
        children = sorted([cols[b] for b in edges[i] if depth[b] > d], key=len, reverse=True)
        if children:
            for j in range(1, len(children)):
                children[0].sumadd(children[j])
            children[0].sumadd({c[i]: 1})
            cols[i] = children[0]
        # max_val = max(cols[i].values())
        answer[i] = cols[i].mx_sum

    print(' '.join(map(str, answer)))


go()