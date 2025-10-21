n, q = list(map(int, input().split()))
servers = [0] * n
for _ in range(q):
    t, k, d = list(map(int, input().split()))
    # free = [i for i, x in enumerate(servers) if x < t]
    free = []
    for sn in range(n):
        if servers[sn] < t:
            free.append(sn)
        if len(free) == k:
            break
    if len(free) < k:
        print(-1)

    else:

        for sn in free:
            servers[sn] = t + d - 1

        print(sum([x + 1 for x in free]))