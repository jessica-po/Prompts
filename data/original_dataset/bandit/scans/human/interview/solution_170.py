n = int(input())
k1 = list(map(int, input().split()[1:]))
k2 = list(map(int, input().split()[1:]))

i = 0
while True:
    if len(k1) == 0 or len(k2) == 0:
        break
    if i > 10000:
        break
    if k1[0] > k2[0]:
        k1 = k1[1:] + k2[0:1] + k1[0:1]
        k2 = k2[1:]
    else:
        k2 = k2[1:] + k1[0:1] + k2[0:1]
        k1 = k1[1:]
    i += 1

if i > 10000:
    print(-1)
else:
    winner = 1
    if len(k1) == 0:
        winner = 2
    print(i, winner)