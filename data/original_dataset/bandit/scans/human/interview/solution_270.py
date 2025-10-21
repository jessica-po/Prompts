n, m = list(map(int, input().split()))
edges_from = [[] for _ in range(n)]
edges_to = [[] for _ in range(n)]

for _ in range(m):
    _from, to = [int(x)-1 for x in input().split()]
    edges_from[_from].append(to)

E_dist_to_goal = [0] * n
P_of_reaching = [0] * n
P_of_reaching[0] = 1

for v in range(n-2, -1, -1):
    routes = edges_from[v]
    for next_v in routes:
        E_dist_to_goal[v] += E_dist_to_goal[next_v] + 1
    E_dist_to_goal[v] /= len(routes)

for v in range(n-1):
    P_now = P_of_reaching[v]
    routes = edges_from[v]
    P_next = P_now / len(routes)
    for next_v in routes:
        P_of_reaching[next_v] += P_next

initial_ans = E_dist_to_goal[0]
answers = [initial_ans]
for v in range(n-2):
    routes = edges_from[v]
    num_of_routes = len(routes)
    if num_of_routes == 1:
        continue
    not_cut_dist = E_dist_to_goal[v]
    longest_dist = max([E_dist_to_goal[next_v]+1 for next_v in routes])
    after_cut_dist = (not_cut_dist - longest_dist/num_of_routes) * num_of_routes / (num_of_routes-1)
    delta = not_cut_dist - after_cut_dist
    candidate = initial_ans - delta * P_of_reaching[v]
    answers.append(candidate)

print((min(answers)))