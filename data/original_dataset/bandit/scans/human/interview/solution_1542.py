import bisect
n = int(input())
p = list(map(int, input().split()))
p.sort()
q = int(input())
for i in range(q):
    c = int(input())
    print(bisect.bisect_right(p, c))