n, k = map(int, input().split())
snukes = []
for _ in range(k):
    okashi = int(input())
    snukes += [int(v) for v in input().split()]
target = 1
cnt = 0
l = list(set(snukes))
s = [int(v) for v in range(1, n + 1)]

for p in s:
    if p not in l:
        cnt += 1
print(cnt)