N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]
for n in range(10**N):
    n = str(n)
    if len(n) != N:
        continue
    if all([n[SC[i][0]-1] == str(SC[i][1]) for i in range(M)]):
        print(n)
        return

print(-1)