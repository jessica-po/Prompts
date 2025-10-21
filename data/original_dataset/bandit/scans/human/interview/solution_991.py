import heapq

city_num, road_num, init_silver = map(int, input().split())
MAX_COST = 2500
init_silver  = min(MAX_COST, init_silver)

G = [[] for _ in range(city_num)]
for _ in range(road_num):
    A, B, cost, time_cost = map(int, input().split())
    A, B = A-1, B-1
    G[B].append([A, cost, time_cost])
    G[A].append([B, cost, time_cost])

for n in range(city_num):
    cost, time_cost = map(int, input().split())
    G[n].append([n, -cost, time_cost])

dp = [[float("inf")] * (MAX_COST+1) for _ in range(city_num)]
dp[0][init_silver] = 0
hq = [(0, 0, init_silver)]
while hq:
    time, node, silver = heapq.heappop(hq)
    for to, silver_cost, time_cost in G[node]:
        remain = min(silver - silver_cost, MAX_COST)
        if remain < 0:
            continue
        dp_next_value = time + time_cost
        if dp[to][remain] <= dp_next_value:
            continue
        dp[to][remain] = dp_next_value
        heapq.heappush(hq, (dp_next_value, to, remain))
print(*[min(d) for d in dp[1:]], sep="\n")