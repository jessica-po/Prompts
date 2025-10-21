q = int(input())
for qi in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    used = [False] * n
    for t in range(n):
        for i in range(len(a) - 1, 0, -1):
            if used[i]:
                continue
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                used[i] = True
    print(' '.join(str(x) for x in a))