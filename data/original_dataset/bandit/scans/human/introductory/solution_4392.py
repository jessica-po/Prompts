for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    p = set(map(int, input().split()))
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1] and j + 1 in p:
                l[j], l[j + 1] = l[j + 1], l[j]
    ans = True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            ans = False
            break
    print('YES' if ans else 'NO')