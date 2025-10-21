from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    l = list(map(int,input().split()))
    if sum(l) == 0:
        print("NO")
    else:
        l.sort()
        if sum(l) > 0:
            l.reverse()
        print("YES")
        print(*l)