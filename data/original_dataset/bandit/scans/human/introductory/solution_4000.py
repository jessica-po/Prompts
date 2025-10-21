import sys
input = sys.stdin.readline

NEGINF = -1000000

n = int(input())
adj = [[] for i in range(n)]
parent = [-1] * n

visited = [False] * n
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

tup = tuple()
outs = [tup] * n
q = [(0, 0)]

while q:
    node, type = q.pop()
    if type == 0:
        visited[node] = True
        q.append((node, 1))
        for v in adj[node]:
            if not visited[v]:
                parent[v] = node
                q.append((v, 0))
    else:
        ones = [(0, node)]
        twos = []
        threes = []
        for v in adj[node]:
            if v != parent[node]:
                a, b, c = outs[v]
                ones.append((a[0] + 1, a[1], v))
                twos.append((b[0] + 1, b[1], v))
                threes.append(c)
        ones.sort(reverse = True)
        twos.sort(reverse = True)
        threes.sort(reverse = True)

        bestOne = (ones[0][0], ones[0][1])
        
        bestsTwo = [(NEGINF, (0, 0))]
        if len(twos) > 0:
            bestsTwo.append((twos[0][0], twos[0][1]))
        if len(ones) > 1:
            o1 = ones[0]
            o2 = ones[1]
            bestsTwo.append((o1[0] + o2[0], (o1[1], o2[1])))

        bestsThree = [(NEGINF, (0, 0, 0))]
        if len(threes) > 0:
            bestsThree.append(threes[0])
        if len(ones) > 2:
            o1 = ones[0]
            o2 = ones[1]
            o3 = ones[2]
            bestsThree.append((o1[0] + o2[0] + o3[0], (o1[1], o2[1], o3[1])))
        if len(twos) > 0:
            o1 = ones[0]
            t1 = twos[0]
            if o1[2] != t1[2]:
                bestsThree.append((o1[0] + t1[0], (o1[1], t1[1][0], t1[1][1])))
            else:
                if len(twos) > 1:
                    t2 = twos[1]
                    bestsThree.append((o1[0] + t2[0], (o1[1], t2[1][0], t2[1][1])))
                if len(ones) > 1:
                    o2 = ones[1]
                    bestsThree.append((o2[0] + t1[0], (o2[1], t1[1][0], t1[1][1])))
                    

        outs[node] = (bestOne, max(bestsTwo), max(bestsThree))

final = outs[0][2]
print(final[0])
print(' '.join([str(x + 1) for x in final[1]]))