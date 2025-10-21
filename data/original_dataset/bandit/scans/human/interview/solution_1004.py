import sys
from collections import Counter
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

S = set()

ans = True
Ans = [] 
cnt = 0
for a in A:
    cnt += 1
    if a > 0:
        S.add(a)
    else:
        a = -a
        if a not in S:
            ans = False
            break
        S.remove(a)
    if not S:
        Ans.append(cnt)
        cnt = 0

if cnt:
    ans = False

if ans:
    A.reverse()
    for c in Ans:
        CA = Counter()
        for _ in range(c):
            CA[abs(A.pop())] += 1
        if any(v > 2 for v in CA.values()):
            ans = False
            break

if ans:
    print(len(Ans))
    print(*Ans)
else:
    print(-1)