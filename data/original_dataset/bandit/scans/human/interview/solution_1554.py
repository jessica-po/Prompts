n = int(input())
cnt = 0
gems = list(map(int, input().split()))
pearls = set()
for i in range(n):
    if gems[i] not in pearls:
        pearls.add(gems[i])
    else:
        cnt += 1
        pearls = set()
    
if cnt:
    print(cnt)
    first = 0
    second = 0
    pearls = set()
    for i in range(n):
        if gems[i] not in pearls:
            pearls.add(gems[i])
        else:
            if second:
                print(first + 1, second + 1)
                first = second + 1
            second = i
            pearls = set()
    print(first + 1, n)
else:
    print('-1')