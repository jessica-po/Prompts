N = int(input())
cnt = [0] * N
for n in range(N - 1):
    u, v = list(map(int, input().split()))
    cnt[u - 1] += 1
    cnt[v - 1] += 1

print(sum(x == 1 for x in cnt))