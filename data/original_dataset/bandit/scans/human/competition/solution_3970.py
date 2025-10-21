n, k = map(int, input().split())
t = list(map(int, input().split()))
if k == 1: print(len(set(t)))
else:
    p = [set() for i in range(30)]
    for i in t:
        j = 0
        while i % k == 0:
            i //= k
            j += 1
        p[j].add(i)
    for j in range(1, 30):
        p[j] -= p[j - 1]
    print(sum(len(i) for i in p))