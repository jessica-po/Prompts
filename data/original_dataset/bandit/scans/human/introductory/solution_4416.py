from sys import stdin

n,k = list(map(int, stdin.readline().strip().split(' ')))

AB = []
A = []
B = []

for i in range(n):
    t,a,b = list(map(int, stdin.readline().strip().split(' ')))
    if a == 1 and b == 1:
        AB.append(t)
    elif a == 1:
        A.append(t)
    elif b == 1:
        B.append(t)

AB.sort()
A.sort()
B.sort()

ans = 0
abi = 0
ai = 0
bi = 0
isPossible = True
for i in range(k):
    if abi == len(AB) and (ai == len(A) or bi == len(B)):
        isPossible = False
        break
    if abi == len(AB):
        ans += (A[ai] + B[bi])
        ai += 1
        bi += 1
        continue
    if ai == len(A) or bi == len(B):
        ans += AB[abi]
        abi += 1
        continue
    if A[ai] + B[bi] <= AB[abi]:
        ans += (A[ai] + B[bi])
        ai += 1
        bi += 1
        continue
    ans += AB[abi]
    abi += 1
    continue
if isPossible:
    print(ans)
else:
    print(-1)